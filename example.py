import bq_consumer as bqc

# En la consola/Notebook verás un DataFrame con la columna mensaje y el valor 'Hola mundo'.
def main():
    # 1. Crear el cliente de BigQuery (usa credenciales del entorno)
    client = bqc.DefaultBigQueryClient()

    # 2. Crear el servicio de consultas
    service = bqc.QueryService(client)

    # 3. Ejecutar una consulta de prueba
    query = "SELECT 'Hola mundo' AS mensaje"
    df = service.fetch_data(query)

    print(df)

if __name__ == "__main__":
    main()
