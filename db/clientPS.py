import psycopg

def client():

    conexion = """
                dbname=postgres
                user=user_postgres
                password=pass_postgres
                host=localhost
                port=5432

                """
    try:
        return psycopg.connect(conexion)
    except Exception as e:
        print(f"Ha habido un error: {e}")

        