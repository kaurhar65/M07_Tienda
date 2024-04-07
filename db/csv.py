from db import clientPS
from Schema import producte


def category(catId, name):
    try:
        conn = clientPS.client()
        cur = conn.cursor()

        cur.execute(f"SELECT * FROM public.category WHERE category_id = {catId}")
        categoriaExiste = cur.fetchone()

        if categoriaExiste:
            cur.execute(f"UPDATE public.category SET name = '{name}', updated_at = CURRENT_TIMESTAMP WHERE category_id = {catId};");
        else:
            cur.execute(f"INSERT INTO public.category(category_id, name, created_at, updated_at) VALUES ({catId}, '{name}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);")
        
        conn.commit()

        return "Todo OK"
    
    except Exception as e:
        return f'Error conexión {e}'    
    finally:
        conn.close()

def subcategory(catId, subId, name):
    try:
        conn = clientPS.client()
        cur = conn.cursor()

        cur.execute(f"SELECT * FROM public.subcategory WHERE subcategory_id = {subId}")
        subCatExiste = cur.fetchone()

        if subCatExiste:
            cur.execute(f"UPDATE public.subcategory SET name='{name}', category_id={catId}, updated_at=CURRENT_TIMESTAMP WHERE subcategory_id={subId};")
        else:
            cur.execute(f"INSERT INTO public.subcategory(subcategory_id, name, category_id, created_at, updated_at) VALUES ({subId}, '{name}', {catId}, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);")
        
        conn.commit()
        return "Todo OK2"
    
    except Exception as e:
        return f'Error conexión {e}'    
    finally:
        conn.close()
    
def product(prodId,name,desc,company,price,units,subCate):
    try:
        conn = clientPS.client()
        cur = conn.cursor()

        cur.execute(f"INSERT INTO public.product(product_id, name, description, company, price, units, subcategory_id, created_at, updated_at) VALUES ({prodId}, '{name}', '{desc}', '{company}', '{price}', '{units}', '{subCate}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);")
        productoExiste = cur.fetchone()

        if productoExiste:
            cur.execute(f"UPDATE public.product SET name='{name}', description='{desc}', company='{company}', price={price}, units={units}, subcategory_id={subCate}, updated_at=CURRENT_TIMESTAMP WHERE product_id={id};")
        else:
            cur.execute(f"INSERT INTO public.product(product_id, name, description, company, price, units, subcategory_id, created_at, updated_at) VALUES ({prodId}, '{name}', '{desc}', '{company}', {price}, {units}, {subCate}, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);")

        conn.commit()
        return "Todo OK3"
    
    except Exception as e:
        return f'Error conexión {e}'
    
    finally:
        conn.close()    