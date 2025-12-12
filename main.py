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

@app.post("/products/", response_model=schemas.ProductResponse , status_code=201,tags=["product"])
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db=db, product=product)

@app.get("/products/", response_model=list[schemas.ProductResponse],tags=["product"])
def read_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_products(db=db, skip=skip, limit=limit)

@app.post("/user",response_model=schemas.UserResponse , status_code=201,tags=["user"])
def create_user(user: schemas.UserCreate, db:Session=Depends(get_db)):
   return crud.create_user(db=db,user=user)

@app.get("/user", response_model=list[schemas.UserResponse],tags=["user"])
def read_user(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_user(db=db, skip=skip, limit=limit)

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

@app.post('/login',status_code=200,tags=['login'])
def login(
   login: schemas.login,
   db: Session=Depends(get_db)
):
   return crud.login(db=db,login=login)

@app.get('/user/{user_id}/order',status_code=200,tags=['order'])
def order(
   user_id: int,
   db: Session=Depends(get_db)
):
    return crud.order(db=db, user_id=user_id)



@app.get('/user/{user_id}/card',response_model=schemas.cardresponse,status_code=200, tags=['card'])
def get_card(
   user_id: int,
   db : Session=Depends(get_db)
):
   return crud.cards(db=db, user_id=user_id)