import os
import psycopg2
import random
from datetime import datetime, timedelta

# Conectar a la base de datos
conn = psycopg2.connect(
    host=os.getenv("DB_HOST", "localhost"),
    database=os.getenv("DB_NAME", "nombre_db"),
    user=os.getenv("DB_USER", "usuario"),
    password=os.getenv("DB_PASS", "contraseña")
)
cursor = conn.cursor()

# Generar 1000 registros para la tabla apartamentos
for i in range(1, 1001):
    numero = i
    ocupado = random.choice([True, False])
    ingreso = random.uniform(1000, 3000) if ocupado else None
    cursor.execute(
        "INSERT INTO apartamentos (numero, ocupado, ingreso) VALUES (%s, %s, %s)",
        (numero, ocupado, ingreso)
    )

# Confirmar los cambios en la tabla apartamentos antes de continuar
conn.commit()

# Recuperar todos los IDs válidos de apartamentos después de confirmar los datos
cursor.execute("SELECT id FROM apartamentos")
apartamento_ids = [row[0] for row in cursor.fetchall()]

# Verificar que tenemos los IDs en apartamento_ids
if not apartamento_ids:
    print("No se encontraron IDs en la tabla apartamentos.")
    conn.close()
    exit()

# Generar registros de mantenimiento (500 registros)
for i in range(1, 501):
    apartamento_id = random.choice(apartamento_ids)  # Usar solo IDs válidos de apartamentos
    fecha_solicitud = datetime.now() - timedelta(days=random.randint(1, 365))
    fecha_resolucion = fecha_solicitud + timedelta(days=random.randint(1, 10)) if random.choice([True, False]) else None
    cursor.execute(
        "INSERT INTO mantenimientos (apartamento_id, fecha_solicitud, fecha_resolucion) VALUES (%s, %s, %s)",
        (apartamento_id, fecha_solicitud, fecha_resolucion)
    )

# Generar registros de encuestas (1000 registros)
for i in range(1, 1001):
    apartamento_id = random.choice(apartamento_ids)  # Usar solo IDs válidos de apartamentos
    puntuacion = random.randint(1, 5)
    cursor.execute(
        "INSERT INTO encuestas (apartamento_id, puntuacion) VALUES (%s, %s)",
        (apartamento_id, puntuacion)
    )

# Confirmar los cambios
conn.commit()

# Cerrar la conexión
cursor.close()
conn.close()

print("Datos de prueba generados correctamente.")
