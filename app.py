import os
import psycopg2
import pandas as pd

# Obtener credenciales desde las variables de entorno
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")

# Conectar a la base de datos PostgreSQL
conn = psycopg2.connect(
    host=db_host,
    port=db_port,
    database=db_name,
    user=db_user,
    password=db_pass
)

# Tasa de ocupación
query_ocupacion = "SELECT COUNT(*) FILTER (WHERE ocupado) / COUNT(*)::float AS tasa_ocupacion FROM apartamentos;"
ocupacion = pd.read_sql(query_ocupacion, conn)

# Ingreso promedio por apartamento ocupado
query_ingreso = "SELECT AVG(ingreso) AS ingreso_promedio FROM apartamentos WHERE ocupado = TRUE;"
ingreso_promedio = pd.read_sql(query_ingreso, conn)

# Tiempo medio de resolución de problemas
query_tiempo_resolucion = """
SELECT AVG(EXTRACT(EPOCH FROM (fecha_resolucion - fecha_solicitud)) / 3600) AS tiempo_promedio_resolucion
FROM mantenimientos WHERE fecha_resolucion IS NOT NULL;
"""
tiempo_resolucion = pd.read_sql(query_tiempo_resolucion, conn)

# Porcentaje de satisfacción del residente
query_satisfaccion = "SELECT AVG(puntuacion) AS satisfaccion_promedio FROM encuestas;"
satisfaccion = pd.read_sql(query_satisfaccion, conn)

# Mostrar resultados
print("Tasa de Ocupación:", ocupacion.iloc[0, 0])
print("Ingreso Promedio por Apartamento Ocupado:", ingreso_promedio.iloc[0, 0])
print("Tiempo Medio de Resolución de Problemas (horas):", tiempo_resolucion.iloc[0, 0])
print("Porcentaje de Satisfacción del Residente:", satisfaccion.iloc[0, 0])

# Cerrar conexión
conn.close()
