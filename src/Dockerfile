# Usa una imagen base oficial de Python
FROM python:3.8-slim

# Establece variables de entorno para soportar UTF-8
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de dependencias al directorio de trabajo actual
COPY requirements.txt ./

# Instala las dependencias del archivo
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de tu aplicacion al directorio de trabajo
COPY . .

# Expone el puerto en el que Gunicorn correrá
EXPOSE 8000

# Comando para ejecutar la aplicacion con Gunicorn
# Asume que tu aplicacion se llama app.py y el objeto de aplicacion es app
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]
