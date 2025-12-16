# To validate 

from pydantic import BaseModel

# to validate the incoming data whether datatype is valid else reject the request
class ProductCreate(BaseModel):
  name:str 
  price:float
  quantity:int


# to validate the response user to get 

class ProductResponse(ProductCreate):
  id:int

  class Config :
    orm_mode=True

'''
Other way -- > 

class ProductResponse(BaseModel):
  id:int 
  name:str 
  price:float
  quantity:int

'''

class UserCreate(BaseModel):
  name:str
  email:str
  phone:str
  password:str
  comformpass:str

class UserResponse(UserCreate):
  id:int

  class Config:
    orm_mode=True



class AddCart(BaseModel):
    userid: int


class cartresponse(AddCart):
    cartid: int

    class Config:
        orm_mode = True

class AddItem(BaseModel):
    productid: int
    quantity: int


class ItemResponse(AddItem):
    itemid: int
    cartid: int

    class Config:
        orm_mode = True


class login(BaseModel):
   email: str
   password: str


class cardresponse(BaseModel):
   cardid : int
   userid: int
   Name: str
   card_no: str
   cvv : int
   pin : int
   expiry: str
   balance: int

   class Config :
      orm_mode =True


class address(BaseModel):
  address: str
  city: str
  state: str
  pincode: str

class AddressResponse(address):
    id: int
    userid: int

    class Config:
        orm_mode = True

class orderplace(BaseModel):
   addressid:int
   paymenttype:str
   cardno:str
   cvv:int
   pin:int
  
class orderresponse(BaseModel):
   orderid:int
   addressid:int
   paymenttype:str
   userid:int
   total:int

   class Config:
      orm_mode=True