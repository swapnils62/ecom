<!--  
pip install fastapi 
pip install uvicorn
 -->

fastapi is the web based framework use to create REST API

REST API :
    1] outer structure
    2] method name
    3] resource path 
  
Ensure that : If same endpoint should have different method and vice versa

### Remember :  apps  is .py file name, app -new varible where we store Fastapi()

# to run server :  uvicorn app:app --reload 

syntax :
@objectname.Method('/endpoint')


pydantic : is the validation lib for validation in fast api
 ---> from pydantic import BaseModel
 



for getting the user input we should mention it in pranthesis of function


# Assignment
1] create get api for user registration
2] create post api for user register 
 dict : name, email ,pass 
check if email already exist 


# to raise the excpetion 

import HTTPException  from fastapi 

and raise the excpetion with specific status code if needed



fastapi -- > To create restapi 
univorn  --> sever
pydantic --> validation
sqlalchemy -- > to convert python to ocm ( object relation mapping)
psycopg2-binary -- > to connect python to postgre Sql


# to run postgre -- > search psql

database.py
   |
models.py
   | 
schema.py 