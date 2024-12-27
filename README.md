# bq_consumer

#### Accede al directorio bq_consumer

```bash
cd bq_consumer 
```

#### Para uso local crear un entorno virtual y activalo 

```bash
python3 -m venv env && source env/bin/activate
```

#### Instala la librería 
```bash
pip install -e .
```

#### Ejecuta el ejemplo 

```bash
python example.py
```

#### Ejecuta en gemini

```bash
!git clone https://github.com/arithgrey/bq_consumer.git
```

#### instalar en gemini 

```bash
!pip install ./bq_consumer
```

#### Si ya se clono y hay actualización 

```bash
!git -C bq_consumer pull
```



#### Completo en Google Colab

```bash
!git clone https://github.com/arithgrey/bq_consumer.git
!pip install ./bq_consumer
cd bq_consumer 
from bq_consumer.query_executor import QueryExecutor

def main():
    # Ejecutar consulta
    query = "SELECT * FROM `findep-calidad-uat-mx.MICROSERVICIOS.serv_caja_unica_acceso_cajas`"
    executor = QueryExecutor()
    df = executor.execute(query)
    
    print(df)

if __name__ == "__main__":
    main()
```
