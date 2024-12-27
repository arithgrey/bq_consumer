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



#### Completo en Google Colab (Pandas)

```bash
!git clone https://github.com/arithgrey/bq_consumer.git
!pip install ./bq_consumer
cd bq_consumer 


from bq_consumer.query_executor import QueryExecutor
import pandas as pd

def main():
    # Ejecutar consulta
    query = "SELECT * FROM `findep-calidad-uat-mx.MICROSERVICIOS.serv_caja_unica_acceso_cajas`"
    executor = QueryExecutor()
    df = executor.execute(query)
    
    # 1. Obtener las primeras y últimas filas del DataFrame
    print("Primeras 5 filas:")
    print(df.head())
    print("\nÚltimas 5 filas:")
    print(df.tail())

    # 2. Filtrar los datos para obtener un subconjunto específico
    filtered_df = df[(df['empresa'] == '000100000000') & (df['monto_cierre_anterior'] > 100)]
    print("\nDatos filtrados:")
    print(filtered_df)

    # 3. Agrupar los datos por una columna y calcular estadísticas
    grouped_df = df.groupby('empresa')['monto_cierre_anterior'].mean()
    print("\nPromedio por empresa:")
    print(grouped_df)

    # 4. Sumarizar los datos con estadísticas descriptivas
    summary_stats = df.describe()
    print("\nEstadísticas descriptivas:")
    print(summary_stats)

    # 5. Calcular el total por columnas numéricas
    total_entradas = df['entradas'].sum()
    total_salidas = df['salidas'].sum()
    print("\nTotal Entradas:", total_entradas)
    print("Total Salidas:", total_salidas)

    # 6. Reemplazar valores nulos con un valor específico
    df['fecha_hora_ini'] = df['fecha_hora_ini'].fillna('2022-01-01 00:00:00')
    print("\nFecha Hora Ini después de reemplazar valores nulos:")
    print(df['fecha_hora_ini'].head())

    # 7. Crear una nueva columna a partir de operaciones matemáticas
    df['diferencia_efectivo'] = df['efectivo_inicial'] - df['efectivo_final']
    print("\nNueva columna 'diferencia_efectivo':")
    print(df[['efectivo_inicial', 'efectivo_final', 'diferencia_efectivo']].head())

    # 8. Ordenar los datos por una columna
    df_sorted = df.sort_values(by='fecha_op')
    print("\nDatos ordenados por 'fecha_op':")
    print(df_sorted[['fecha_op', 'id_caja']].head())

    # 9. Calcular correlaciones entre columnas numéricas
    # Eliminar filas con valores nulos en las columnas relevantes antes de calcular la correlación
    correlation = df[['monto_cierre_anterior', 'entradas']].dropna().corr()
    print("\nCorrelación entre monto_cierre_anterior y entradas:")
    print(correlation)

    # 10. Convertir una columna de fechas en un tipo datetime y extraer información de la fecha
    df['fecha_op'] = pd.to_datetime(df['fecha_op'])
    df['anio'] = df['fecha_op'].dt.year
    df['mes'] = df['fecha_op'].dt.month
    print("\nFecha op con año y mes extraídos:")
    print(df[['fecha_op', 'anio', 'mes']].head())

if __name__ == "__main__":
    main()

```


#### Completo en Google Colab (Pandas + numpy)
```bash
!git clone https://github.com/arithgrey/bq_consumer.git
!pip install ./bq_consumer
cd bq_consumer


from bq_consumer.query_executor import QueryExecutor
import pandas as pd
import numpy as np

def main():
    # Ejecutar consulta
    query = "SELECT * FROM `findep-calidad-uat-mx.MICROSERVICIOS.serv_caja_unica_acceso_cajas`"
    executor = QueryExecutor()
    df = executor.execute(query)
    
    # 1. Obtener las primeras y últimas filas del DataFrame
    print("Primeras 5 filas:")
    print(df.head())
    print("\nÚltimas 5 filas:")
    print(df.tail())

    # 2. Filtrar los datos para obtener un subconjunto específico
    filtered_df = df[(df['empresa'] == '000100000000') & (df['monto_cierre_anterior'] > 100)]
    print("\nDatos filtrados:")
    print(filtered_df)

    # 3. Agrupar los datos por una columna y calcular estadísticas
    grouped_df = df.groupby('empresa')['monto_cierre_anterior'].mean()
    print("\nPromedio por empresa:")
    print(grouped_df)

    # 4. Sumarizar los datos con estadísticas descriptivas
    summary_stats = df.describe()
    print("\nEstadísticas descriptivas:")
    print(summary_stats)

    # 5. Calcular el total por columnas numéricas
    total_entradas = df['entradas'].sum()
    total_salidas = df['salidas'].sum()
    print("\nTotal Entradas:", total_entradas)
    print("Total Salidas:", total_salidas)

    # 6. Reemplazar valores nulos con un valor específico usando pandas
    df['fecha_hora_ini'] = df['fecha_hora_ini'].fillna('2022-01-01 00:00:00')
    print("\nFecha Hora Ini después de reemplazar valores nulos:")
    print(df['fecha_hora_ini'].head())

    # 7. Crear una nueva columna a partir de operaciones matemáticas usando Numpy
    df['diferencia_efectivo'] = np.subtract(df['efectivo_inicial'], df['efectivo_final'])
    print("\nNueva columna 'diferencia_efectivo' usando Numpy:")
    print(df[['efectivo_inicial', 'efectivo_final', 'diferencia_efectivo']].head())

    # 8. Ordenar los datos por una columna
    df_sorted = df.sort_values(by='fecha_op')
    print("\nDatos ordenados por 'fecha_op':")
    print(df_sorted[['fecha_op', 'id_caja']].head())

    # 9. Calcular correlaciones entre columnas numéricas usando Numpy
    # Eliminar filas con valores nulos en las columnas relevantes antes de calcular la correlación
    cleaned_df = df[['monto_cierre_anterior', 'entradas']].dropna()

    # Verificar si alguna columna contiene solo valores constantes
    if cleaned_df['monto_cierre_anterior'].std() != 0 and cleaned_df['entradas'].std() != 0:
        correlation = np.corrcoef(cleaned_df['monto_cierre_anterior'], cleaned_df['entradas'])
        print("\nCorrelación entre monto_cierre_anterior y entradas usando Numpy:")
        print(correlation)
    else:
        print("\nNo se puede calcular la correlación: una de las columnas tiene solo valores constantes o nulos.")

    # 10. Convertir una columna de fechas en un tipo datetime y extraer información de la fecha
    df['fecha_op'] = pd.to_datetime(df['fecha_op'])
    df['anio'] = df['fecha_op'].dt.year
    df['mes'] = df['fecha_op'].dt.month
    print("\nFecha op con año y mes extraídos:")
    print(df[['fecha_op', 'anio', 'mes']].head())

if __name__ == "__main__":
    main()
 
```
