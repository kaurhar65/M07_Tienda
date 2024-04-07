from typing import Union
from model import Product
from db import productDB, csv
from fastapi import File, UploadFile, FastAPI
import pandas as pd

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

@app.post("/loadProducts")
async def loadProductes(file: UploadFile):
    datosFichero = pd.read_csv(file.file, header=0)
    for i, row in datosFichero.iterrows():
        j = row.to_dict()
        category(j["id_categoria"], j["nom_categoria"])
        subcategory(j["id_categoria"], j["id_subcategoria"], j["nom_subcategoria"])
        product(j["id_producto"], j["nom_producto"], j["descripcion_producto"], j["companyia"], j["precio"],j["unidades"], j["id_subcategoria"])
    return {"message": "introducidos los datos de forma correcta"}

def category(id, name):
    return csv.category(id, name)

def subcategory(idCAt, id, name):
    return csv.subcategory(idCAt, id, name)

def product(id, name, desc, company, price, unit, idSubcate):
    return csv.product(id, name, desc, company, price, unit, idSubcate)