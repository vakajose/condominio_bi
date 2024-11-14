# Usar una imagen de Python como base
FROM python:3.9-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de Python
COPY app.py .

# Instalar dependencias
RUN pip install psycopg2-binary pandas

# Ejecutar el script principal
CMD ["python", "app.py"]
