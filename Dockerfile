# Usa una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo de la aplicación desde la carpeta `app` en el host
COPY app/app.py /app/app.py
COPY app/templates /app/templates

# Instala boto3 y flask para la conexión a DynamoDB y el servidor web
RUN pip install boto3 flask

# Ejecuta el archivo de la aplicación
CMD ["python", "app.py"]
