from typing import Union
from fastapi import FastAPI
from model import Product
from db import clientPS
from db import productDB

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/product/")
def getAllProducts():
    return productDB.getAllProducts()

@app.get("/product/{id}")
def getProductById(id):
    return productDB.getProductById(id)

@app.get("/productAll/")
def getAllProducts():
    return productDB.getAllProductsMasEspecifico()

@app.post("/product/")
def insertProduct(prod: Product.Product):
    return productDB.insertProduct(prod.id,prod.name,prod.description,prod.company,prod.price,prod.unit,prod.subcategory_id)
    
@app.put("/product/{id}")
def updateProductById(prod: Product.Product):    
    return productDB.updateProductById(prod)

@app.delete("/product/{id}")
def deleteProductByID(id):
    return productDB.deleteProductByID(id);
