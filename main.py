#Import thr FASTAPI class
from fastapi import FastAPI

#create an instance of the FastAPI class. 
app = FastAPI()

#Define a path operation decorator
@app.get("/")
#define the path operation function
async def root():
    #returen the content
    return {"message": "Hello World!"}

#you can create another endpoint just as easily
@app.get("/welcome")
async def welcome_user(name: str = "Guest"):
    return {"Message": f"Hello, {name}! Welcome to our API."}
