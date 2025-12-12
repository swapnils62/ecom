
# Static api : Don't refer 



# run server :  uvicorn app:app --reload 


from fastapi import FastAPI , HTTPException 
from pydantic import BaseModel


app=FastAPI()

class Products(BaseModel):
    id:int 
    name:str
    price:int 

class registerUser(BaseModel):
    name:str
    email:str
    password:str

register=[]

products=[{
    "id":1,
    "name":"Smartwatch",
    "price":2999},
    {
    "id":2,
    "name":"Noisebuds",
    "price":1999},
    {
    "id":3,
    "name":"Headphone",
    "price":5000
    }]

# testing api
@app.get("/")
def root():
    return {"Hello from first API"}

# api to get all products
@app.get("/products")
def Product():
    return products

# api to get product by id
@app.get("/products/{product_id}")
def Products_by_id(product_id:int):
    for product in products:
        if product['id'] == product_id:
            return product
    return "Invalid product id"

# api to add product
@app.post("/addProduct")
def add_product(product:Products):  # -- > Validate the user data with above mention datatype in Products
    for product_data in products:
        if product_data["id"]==product.id :
            # return "Product id already exists"
            raise HTTPException(status_code=404,detail=f"Product id {product.id} already exists")
    products.append(product)  # --> convert pydantic model to dictionary
    # return "Added product sucessfully"
    raise HTTPException(status_code=201,detail=f"{product} added successfully")

# Api to register user
@app.post("/users/login")
def user_login(reg:registerUser):
    for i in register:
        if i["email"] in reg.email:
            return "Email already exists"
    register.append(reg.dict())
    return "User registered successfully" 

# Api to get all registered users
@app.get("/users")
def get_users():
    return register