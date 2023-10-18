# Utiliza una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo en la carpeta de la aplicación
WORKDIR /app

# Copia los archivos de requisitos e instala las dependencias
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copia el código de la aplicación a la imagen
COPY . .

# Expone el puerto en el que se ejecutará la aplicación
EXPOSE 8000

# Inicia la aplicación usando Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
