# actual to create api 

from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy.orm import Session
import models,schemas,crud
from database import engine,SessionLocal,Base

# create table if not exist
Base.metadata.create_all(bind=engine)

app=FastAPI(
   title="Ecom project",
   description='''
      [Baseurl=http://127.0.0.1:800/]

'''
)

# Dependency for db 

# Bind the database -- > db is used 

def get_db():
  db=SessionLocal()
  try :
    yield db 
  finally :
    db.close()

#====================api for product =========================

@app.post("/products/", response_model=schemas.ProductResponse , status_code=201,tags=["product"])
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db=db, product=product)

@app.get("/products/", response_model=list[schemas.ProductResponse],tags=["product"])
def read_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_products(db=db, skip=skip, limit=limit)




# ==============api for user ========================

@app.post("/user",response_model=schemas.UserResponse , status_code=201,tags=["user"])
def create_user(user: schemas.UserCreate, db:Session=Depends(get_db)):
   return crud.create_user(db=db,user=user)

@app.get("/user", response_model=list[schemas.UserResponse],tags=["user"])
def read_user(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_user(db=db, skip=skip, limit=limit)


# ===================api for user login ==============

@app.post('/login',status_code=200,tags=['login'])
def login(
   login: schemas.login,
   db: Session=Depends(get_db)
):
   return crud.login(db=db,login=login)


#============api for address creation====================
@app.post('/user/{userid}/address', response_model=schemas.AddressResponse,status_code=201, tags=['address'])
def add_address(
   userid:int,
   address:schemas.address, 
   db:Session=Depends(get_db)
   ):
   return crud.add_address(db=db,address=address,userid=userid)




@app.get('/user/{userid}/address',response_model=list[schemas.AddressResponse],tags=['address'])
def get_address(
   userid: int,
   skip: int=0,
   limit: int=10,
   db: Session=Depends(get_db),
):
   return crud.get_address(db=db,skip=skip,limit=limit,userid=userid)


#=====================api for user cart================

@app.post("/user/cart", response_model=schemas.cartresponse, status_code=201, tags=["cart"])
def create_cart(
    cart: schemas.AddCart,
    db: Session = Depends(get_db),
):
    return crud.addcart(db=db, cart=cart)

@app.post('/user/{user_id}/cart/{cart_id}/item', response_model=schemas.ItemResponse, status_code=201, tags=['cart'])
def add_item(
   user_id :int,
   cart_id : int,
   item : schemas.AddItem,
   db: Session =Depends(get_db)
):
   return crud.add_item(db=db, item=item,user_id=user_id,cart_id=cart_id)




#==================== api for user orders======================= 

@app.get('/user/{user_id}/carttotal',status_code=200,tags=['carttotal'])
def order(
   user_id: int,
   db: Session=Depends(get_db)
):
    return crud.cart_total(db=db, user_id=user_id)


#==============api for order palce =============
@app.post('/user/{userid}/order',response_model=schemas.orderresponse,status_code=201,tags=['Place order'])
def order_place(userid:int,orderplace:schemas.orderplace,db:Session=Depends(get_db)):
   return crud.order(db=db,userid=userid,orderplace=orderplace)


# ========================api for card generator====================

@app.get('/user/{user_id}/card',response_model=schemas.cardresponse,status_code=200, tags=['card'])
def get_card(
   user_id: int,
   db : Session=Depends(get_db)
):
   return crud.cards(db=db, user_id=user_id)

