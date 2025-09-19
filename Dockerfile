FROM python:3.12-slim

# Variables de entorno para que Python no genere archivos innecesarios
ENV PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Instalar MkDocs + Material + ghp-import
RUN pip install --no-cache-dir mkdocs mkdocs-material ghp-import

# Directorio de trabajo dentro del contenedor
WORKDIR /site

# Exponer el puerto 8000
EXPOSE 8000

# Comando por defecto para levantar el servidor
CMD ["mkdocs", "serve", "-a", "0.0.0.0:8000"]
