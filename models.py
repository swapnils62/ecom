#  structural files to store details about the tables in database

from sqlalchemy import Column,String,Float,Integer,ForeignKey
from database import Base

# products -- > table name  & __tablename__ : attribute to create a table 


# ============product table====================

class Product(Base):
  __tablename__="products"

# mention column name

  id=Column(Integer,primary_key=True,index=True)
  name=Column(String,nullable=False)
  price=Column(Float,nullable=False)
  quantity=Column(Integer,nullable=False)


# ==============user table ================

class Users(Base):
  __tablename__='users'

  id=Column(Integer,primary_key=True,index=True)
  name=Column(String,nullable=False)
  email=Column(String,unique=True,nullable=False)
  phone=Column(String,nullable=False,unique=True)
  password=Column(String,nullable=False)
  comformpass=Column(String,nullable=False)


# ================cart teble =================

class Cart(Base):
  __tablename__='cart'

  cartid=Column(Integer,primary_key=True,index=True)
  userid=Column(Integer,ForeignKey("users.id"))

# ==============cart item table ===============

class CartItem(Base):
  __tablename__='cartitem'

  itemid=Column(Integer,primary_key=True,index=True)
  cartid=Column(Integer,ForeignKey('cart.cartid'))
  productid=Column(Integer,ForeignKey('products.id'))
  quantity=Column(Integer,nullable=False)



# ================card table================
class Card(Base):
  __tablename__='cards'

  cardid=Column(Integer, primary_key=True,index=True)
  userid=Column(Integer,ForeignKey("users.id"))
  Name=Column(String,nullable=False)
  card_no=Column(String(16),nullable=False,unique=True)
  cvv=Column(Integer,nullable=False,unique=True)
  pin=Column(Integer,nullable=False)
  expiry=Column(String,nullable=False)
  balance=Column(Integer,nullable=False)




class Address(Base):
  __tablename__='address'

  id=Column(Integer,primary_key=True,index=True)
  userid=Column(Integer,ForeignKey('users.id'))
  address=Column(String,nullable=False)
  city=Column(String,nullable=False)
  state=Column(String,nullable=False)
  pincode=Column(String,nullable=False)


class Order(Base):
  __tablename__='order'
  orderid=Column(Integer,primary_key=True,index=True)
  userid=Column(Integer,ForeignKey('users.id'))
  addressid=Column(Integer,ForeignKey('address.id'))
  paymenttype=Column(String,nullable=False)
  total=Column(Integer,nullable=False)
  status=Column(String,nullable=False)

class orderitem(Base):
  __tablename__='orderitem'
  itemid=Column(Integer,primary_key=True,index=True)
  orderid=Column(Integer,ForeignKey('order.orderid'))
  productid=Column(Integer,ForeignKey('products.id'))
  quantity=Column(Integer,nullable=False)
  price=Column(Integer,nullable=False)
  subtotal=Column(Integer,nullable=False)





# =======================wishlist table =============
class wishlist(Base):
  __tablename__='wishlist'
  id=Column(Integer,primary_key=True,index=True)
  userid=Column(Integer,ForeignKey('users.id'))

class wishlist_item(Base):
  __tablename__='wishlistitem'
  id=Column(Integer,primary_key=True,index=True)
  wishlistid=Column(Integer,ForeignKey('wishlist.id'))
  productid=Column(Integer,ForeignKey('products.id'))

