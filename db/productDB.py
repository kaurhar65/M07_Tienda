import json
from db import clientPS
from Schema import producte
from model.Product import Product
import psycopg

def getAllProducts():
    try:
        conn = clientPS.client()
        cur = conn.cursor()
        cur.execute("SELECT * FROM public.product")
        data = cur.fetchall()
        data = producte.product_schema(data)

    except Exception as e:
        return f'Error conexión {e}'
    
    finally:
        conn.close()
        return f"consulta de {data}"

def getProductById(id:int):
    try:
        conn = clientPS.client()
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM public.product where product_id = {id}")
        data = cur.fetchone()
        data = producte.product_schema(data)

    except Exception as e:
        return f'Error conexión {e}'
    
    finally:
        conn.close()
        return f"consulta de {data}"



def insertProduct(id,name,desc,company,price,units,subCate):
    try:
        conn = clientPS.client()
        cur = conn.cursor()
        cur.execute(f"INSERT INTO public.product(product_id, name, description, company, price, units, subcategory_id, created_at, updated_at) VALUES ({id}, '{name}', '{desc}', '{company}', '{price}', '{units}', '{subCate}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);")
        conn.commit()

    except Exception as e:
        return f'Error conexión {e}'
    
    finally:
        conn.close()    
    return f"Producto añadido"


def updateProductById(prod):
    try:
        conn = clientPS.client()
        cur = conn.cursor()
        cur.execute(f"UPDATE public.product SET name = '{prod.name}', description = '{prod.description}', company = '{prod.company}', price = {prod.price}, units = {prod.unit}, subcategory_id = {prod.subcategory_id}, updated_at=CURRENT_TIMESTAMP WHERE product_id = {prod.id}")

        conn.commit()

        return {"message": "Producte actualitzat correctament", "state": 200}

    except Exception as e:
        print(f'ERROR: {e}')
        conn.rollback()
        return {"message": f"Error al actualitzar el producte: {str(e)}", "state": 500}
    finally:
        conn.close()

def deleteProductByID(id:int):
    try:
        conn = clientPS.client()
        cur = conn.cursor()
        cur.execute(f"DELETE from public.product where product_id={id}")
        conn.commit()
        
    except Exception as e:
        return f'Error conexión: {e}'
    
    finally:
        conn.close()    
        return f"Producto eliminado"


def getAllProductsMasEspecifico():
    try:
        conn = clientPS.client()
        cur = conn.cursor()
        cur.execute("""
                    SELECT c.name AS category_name,s.name AS subcategory_name,p.name AS product_name,p.company AS product_brand,p.price AS product_price
                    FROM product p JOIN subcategory s ON p.subcategory_id = s.subcategory_id JOIN 
                    category c ON s.category_id = c.category_id;""")
        
        data =cur.fetchall()
        json_data = []
        for row in data:
            json_data.append({
                'category_name': row[0],
                'subcategory_name': row[1],
                'product_name': row[2],
                'product_brand': row[3],
                'product_price': float(row[4])
            })

        return json.dumps(json_data)
         
    except Exception as e:
        return f'Error conexión {e}'    
    finally:
        conn.close()