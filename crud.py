# for execution based on the endpoints 

from sqlalchemy.orm import Session
import models,schemas
from fastapi import HTTPException
from pass_hash import Hashpass, verify
from card import cardno_generator,cvv_generator,pin_generator

# product:schemas.ProductCreate -- > Validates the input of user and store in product

def create_product(db:Session,product:schemas.ProductCreate) :

  # to enter the user data in column
  db_product=models.Product(

    # name --> column name & product.name --> name of product [entered by user]

    name=product.name ,
    price=product.price,
    quantity=product.quantity
  )
  

  # finally data enters and commit 
  db.add(db_product)
  db.commit()
  db.refresh(db_product)

  return db_product     # return the product details entered by user

#  method to get product
 
 # to get the data in set of 10 , limit & skip is used  --> named pagination
 # and return same as select * from products in sql 

def get_products(db:Session,skip:int=0,limit:int=10):
  return db.query(models.Product).offset(skip).limit(limit).all()



# =============================api for user creation======================



def create_user(db:Session, user:schemas.UserCreate):
  
  # first check password match or not
  if user.password!=user.comformpass:
     raise HTTPException(status_code=400, detail="password not match")
  
  # check for user alrady exist or not 
  existing_user = db.query(models.Users).filter(models.Users.email == user.email).first()
  if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
  
  hashpass=Hashpass(user.password)


  db_user=models.Users(
    name=user.name,
    email=user.email,
    phone=user.phone,
    password=hashpass,
    comformpass=hashpass
  )

  db.add(db_user)
  db.commit()
  db.refresh(db_user)
  return db_user

def get_user(db:Session,skip:int=0,limit:int=10):
  return db.query(models.Users).offset(skip).limit(limit).all()



# =====================api for cart creation=========================

def addcart(db: Session, cart: schemas.AddCart) -> schemas.cartresponse:
    # 1. check user exists
    user = db.query(models.Users).filter(models.Users.id == cart.userid).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # 2. check if user already has a cart
    usercart = db.query(models.Cart).filter(models.Cart.userid == cart.userid).first()
    if usercart:
       raise HTTPException(status_code=400, detail="Cart already present for this user")
    
    # 3. create new cart
    newcart = models.Cart(userid=cart.userid)

    db.add(newcart)
    db.commit()
    db.refresh(newcart)

    # 4. return response (cartid + userid only)
    return schemas.cartresponse(
        cartid=newcart.cartid,   # use cartid from Cart model
        userid=newcart.userid
    )


# ====================api for cartitem==========================


def add_item(db: Session, item : schemas.AddItem, user_id : int, cart_id: int):
   
   # first find the user car with user id 
   cart= db.query(models.Cart).filter(models.Cart.cartid==cart_id, models.Cart.userid==user_id).first()
   if not cart:
      raise HTTPException(status_code=404, detail='cart not found for this user')
   
   #then check for the product exsit or not
   product=db.query(models.Product).filter(models.Product.id==item.productid).first()
   if not product:
      raise HTTPException(status_code=404, detail='product not found')
   
   # then check for the quantity of product is grater then user given quantity
   if product.quantity<item.quantity:
      raise HTTPException(status_code=400, detail=f'out of stock the availabe qty is{product.quantity}')
   
   # after that check the product is alrady prsent in cart or not if present then incress the quantity  
   # else add new product in the cart
   alradyproduct=db.query(models.CartItem).filter(models.CartItem.cartid==cart_id,models.CartItem.productid==item.productid).first()
   if alradyproduct:
      alradyproduct.quantity+=item.quantity
      product.quantity-=item.quantity
      db.commit()
      return alradyproduct
   

   product.quantity-=item.quantity

   cart_item=models.CartItem(
      cartid=cart_id,
      productid=item.productid,
      quantity=item.quantity

   )
   db.add(cart_item)
   db.commit()
   db.refresh(cart_item)
   return cart_item



# =====================api for user login =======================

def login(db:Session, login:schemas.login):
   
   user=db.query(models.Users).filter(models.Users.email==login.email).first()
   if not user :
      raise HTTPException(status_code=404,detail='invalid email')
   if verify(user.password, login.password)!=True:
        raise HTTPException(status_code=401, detail="Invalid password")
   return 'login sucessfull'



# ======================api for orders========================

def order(db:Session, user_id:int):

   # check user is present or not
   user=db.query(models.Users).filter(models.Users.id==user_id).first()
   if not user :
      raise HTTPException(status_code=404, detail='user not found')
   
   # find the cart for the user 
   user_cart=db.query(models.Cart).filter(models.Cart.userid==user_id).first()
   if not user_cart:
      raise HTTPException(status_code=404, detail='cart not found for user')
   
   # find the all the cart item present in the cart 
   cart_item=db.query(models.CartItem).filter(models.CartItem.cartid==user_cart.cartid).all()
   if not cart_item:
      raise HTTPException(status_code=404, detail="item not added")
   
   # make the total of all product price
   total=0
   for i in cart_item:
      product=db.query(models.Product).filter(models.Product.id==i.productid).first()
   
      total=total+product.price*i.quantity
   return cart_item,f"Grand total={total}"



# ==========================api for debit card details==================

def cards(db:Session, user_id:int):
   user=db.query(models.Users).filter(models.Users.id==user_id).first()
   if not user:
      raise HTTPException(status_code=404, detail='user not found')
   cardno=cardno_generator()
   cvv=cvv_generator()
   pin=pin_generator()

   db_card=models.Card(
      Name=user.name,
      userid=user_id,
      card_no=cardno,
      cvv=cvv,
      pin=pin,
      expiry='12/30',
      balance=1000000
   )

   db.add(db_card)
   db.commit()
   db.refresh(db_card)
   return db_card