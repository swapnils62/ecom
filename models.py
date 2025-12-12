#  structural files to store details about the tables in database

from sqlalchemy import Column,String,Float,Integer,ForeignKey
from database import Base

# products -- > table name  & __tablename__ : attribute to create a table 

class Product(Base):
  __tablename__="products"

# mention column name

  id=Column(Integer,primary_key=True,index=True)
  name=Column(String,nullable=False)
  price=Column(Float,nullable=False)
  quantity=Column(Integer,nullable=False)

class Users(Base):
  __tablename__='users'

  id=Column(Integer,primary_key=True,index=True)
  name=Column(String,nullable=False)
  email=Column(String,unique=True,nullable=False)
  phone=Column(String,nullable=False,unique=True)
  password=Column(String,nullable=False)
  comformpass=Column(String,nullable=False)

class Cart(Base):
  __tablename__='cart'

  cartid=Column(Integer,primary_key=True,index=True)
  userid=Column(Integer,ForeignKey("users.id"))

class CartItem(Base):
  __tablename__='cartitem'

  itemid=Column(Integer,primary_key=True,index=True)
  cartid=Column(Integer,ForeignKey('cart.cartid'))
  productid=Column(Integer,ForeignKey('products.id'))
  quantity=Column(Integer,nullable=False)