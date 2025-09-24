# Proceso de creación con MkDocs

## 1. Instalación de MkDocs

**Comando usado:**

```bash
pip install mkdocs
```

**Resultado:** Se instaló MkDocs en mi entorno virtual correctamente.

**Comprobación de la instalación:**

```bash
mkdocs --version
```

---

## 2. Creación del proyecto base

**Comando usado:**

```bash
mkdocs new .
```

**Resultado:** Se generó el archivo `mkdocs.yml` y la carpeta `docs/` con el archivo inicial `index.md`.

---

## 3. Creación de una nueva página

En la carpeta `docs/` creé un nuevo archivo:

```text
proceso.md
```

**Resultado:** Ahora tengo dos páginas en la documentación: `index.md` y `proceso.md`.

---

## 4. Configuración de la navegación

**Archivo editado:** `mkdocs.yml`

**Configuración añadida:**

```yaml
site_name: Documentación de Alejandro

nav:
  - Inicio: index.md
  - Proceso: proceso.md
```

**Resultado:** Al recargar el servidor se muestran en la barra de navegación las dos páginas: **Inicio** y **Proceso**.

---

## 5. Servir la documentación en local

**Comando usado:**

```bash
mkdocs serve
```

**Resultado:** El servidor se levantó en `http://127.0.0.1:8000` y pude ver la documentación funcionando con las dos páginas.

---

## 6. Subida del proyecto a GitHub

**Comando usado para crear el README y hacer el primer commit:**

```bash
echo "# alejandro-documentacion" >> README.md
git init
git add README.md
git commit -m "first commit"
```

**Resultado:** Se creó el archivo `README.md`, se inicializó el repositorio Git en local y se hizo el primer commit.

**Comando usado para crear la rama principal y enlazar el remoto:**

```bash
git branch -M main
git remote add origin https://github.com/alepe03/alejandro-documentacion.git
```

**Resultado:** El repositorio local quedó enlazado con el remoto en GitHub en la rama `main`.

**Comando usado para subir el commit inicial:**

```bash
git push -u origin main
```

**Resultado:** El proyecto se subió correctamente a GitHub en la rama `main`.

---

## 7. Añadir el proyecto de MkDocs al repositorio

**Comandos usados:**

```bash
git add .
git commit -m "docs: añade estructura MkDocs (mkdocs.yml, docs/)"
git push
```

**Resultado:** Se añadieron los archivos de MkDocs (`mkdocs.yml`, `docs/index.md`, `docs/proceso.md`, etc.) al repositorio remoto.

---

## 8. Publicación en GitHub Pages

**Comando usado para generar y desplegar el sitio:**

```bash
mkdocs gh-deploy --force
```

**Resultado:** MkDocs compiló el sitio, generó la carpeta `site/` y publicó el contenido en la rama `gh-pages` del repositorio.

---

## 9. Activación de GitHub Pages

En GitHub, entré a **Settings → Pages**.  
Seleccioné como **Source** la rama `gh-pages` y carpeta `/ (root)`.  
Guardé los cambios.  

**Resultado:** GitHub Pages quedó activado y me proporcionó la URL pública del sitio.

**URL de la documentación:**  
👉 [https://alepe03.github.io/alejandro-documentacion/](https://alepe03.github.io/alejandro-documentacion/)

---

## 10. Verificación final

Abrí la URL pública en el navegador y comprobé que la documentación generada con MkDocs está visible online.

---

## 11. Aplicación de una plantilla estética (Material for MkDocs)

### 11.1 Instalación del tema Material
**Comando usado:**
```bash
pip install mkdocs-material
```
añadimos el tema en **mkdocs.yml**:

```bash
site_name: Documentación de Alejandro

nav:
  - Inicio: index.md
  - Proceso: proceso.md

theme:
  name: material
```
**Resultado:** Al volver a ejecutar el servidor con:
```bash
mkdocs serve
```
la documentación cambió automáticamente a la estética del tema Material, mostrando un diseño más moderno y visual.

---

## 12. Uso de Docker para la documentación

### 12.1 Creación del Dockerfile

Creé un archivo llamado `Dockerfile` en la raíz del proyecto con el siguiente contenido:

```dockerfile
FROM python:3.12-slim

# Variables de entorno para que Python no genere archivos innecesarios
ENV PIP_DISABLE_PIP_VERSION_CHECK=1     PYTHONDONTWRITEBYTECODE=1     PYTHONUNBUFFERED=1

# Instalar MkDocs + Material + ghp-import
RUN pip install --no-cache-dir mkdocs mkdocs-material ghp-import

# Directorio de trabajo dentro del contenedor
WORKDIR /site

# Exponer el puerto 8000
EXPOSE 8000

# Comando por defecto para levantar el servidor
CMD ["mkdocs", "serve", "-a", "0.0.0.0:8000"]
```

**Resultado:** Dockerfile preparado para construir una imagen con Python, MkDocs y el tema Material.


### 12.2 Creación del archivo docker-compose.yml

Creé un archivo `docker-compose.yml` con el siguiente contenido:

```yaml
services:
  mkdocs:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - ./:/site
    command: mkdocs serve -a 0.0.0.0:8000
```

**Resultado:** Configuración lista para levantar el servidor de MkDocs de forma sencilla con un solo comando.

### 12.3 Construcción de la imagen

**Comando usado:**

```bash
docker compose build
```

**Resultado:** Se construyó la imagen de Docker con Python 3.12, MkDocs, Material y ghp-import.  
La consola mostró la descarga de la imagen base y la instalación de dependencias.


### 12.4 Levantar el servidor dentro del contenedor

**Comando usado:**

```bash
docker compose up
```

**Resultado:** El sitio de documentación se sirvió correctamente en `http://localhost:8000`, ejecutándose dentro de un contenedor Docker.


### 12.5 Parar y limpiar contenedores

**Comandos usados:**

```bash
# detener el servidor
CTRL + C

# eliminar contenedores y red
docker compose down
```

**Resultado:** El contenedor se detuvo y se liberaron los recursos de Docker.

---

## 13. Operaciones avanzadas en Git (ejecutadas)

>Estas operaciones las realicé en el repositorio `alejandro-documentacion`.


iniciar bisect
```bash
git bisect start
```
marcar el commit actual como **"malo"**
```bash
git bisect bad
```

marcar un commit antiguo donde todo funcionaba como **"bueno"**
```bash
git bisect good <...>
```

Git me lleva a un punto intermedio; probé el sitio **(mkdocs serve)**
```bash
git bisect bad   **fallaba**
```

repetí el proceso hasta que Git dio el primer commit malo

**al terminar:**
```bash
git bisect reset
```
---

## 14. Seguridad en los sistemas de control de versiones

### 14.1 Uso de `.gitignore` para evitar subir archivos innecesarios
Creé un archivo `.gitignore` en la raíz del proyecto con el siguiente contenido:

```text
site/
__pycache__/
.DS_Store
.env
```

---

## 15. Integración continua (CI/CD) con GitHub Actions

### 15.1 Creación del workflow de despliegue automático
Creé el archivo `.github/workflows/mkdocs.yml` con el contenido:

```bash
name: Build & Deploy MkDocs

on:
  push:
    branches: [ main ]

permissions:
  contents: write

jobs:
  build-deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout código
        uses: actions/checkout@v4

      - name: Configurar Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Instalar dependencias
        run: pip install mkdocs mkdocs-material ghp-import

      - name: Compilar documentación
        run: mkdocs build --strict

      - name: Desplegar en GitHub Pages
        run: mkdocs gh-deploy --force
```

**Resultado:** En cada push a main, GitHub Actions compila la documentación y publica automáticamente en la rama gh-pages.

---

## 16. Desarrollo y documentación de la librería matemática

### 16.1 Integración de la librería
Integré la carpeta `maths/` del repositorio de ejemplo `sphinx_basics` dentro de mi proyecto `alejandro-documentacion`.  
La librería contiene cuatro funciones matemáticas básicas: `add`, `subtract`, `multiply` y `divide`.

---

### 16.2 Cambios realizados
- Todas las funciones fueron modificadas para aceptar un número indefinido de argumentos mediante `*args`.
- La lógica de cada función se adaptó al nuevo esquema:
  - `add` ahora suma todos los argumentos.
  - `subtract` resta de manera secuencial.
  - `multiply` multiplica todos los valores.
  - `divide` divide de forma secuencial, comprobando que no se divida entre cero.
- Los **docstrings** fueron actualizados para documentar el uso de `*args` y proporcionar ejemplos de uso.

---

### 16.3 Ejemplos documentados
Los docstrings incluyen ejemplos claros:

```python
>>> add(2, 3, 5)
10

>>> subtract(100, 20, 30, 40)
10

>>> multiply(2, 3, 4)
24

>>> divide(100, 2, 5)
10.0
```

## 16.4 Pruebas realizadas
Probé las funciones desde la consola de Python:

```python
from maths import add, subtract, multiply, divide

print(add(2, 3, 5))             # 10
print(subtract(100, 20, 30, 40)) # 10
print(multiply(2, 3, 4))         # 24
print(divide(100, 2, 5))         # 10.0
```

**Resultado:** Todas las funciones funcionan correctamente con múltiples argumentos y los ejemplos documentados son congruentes con los cambios realizados.

---

## 17. Pruebas de la librería matemática

### 17.1 Creación de un script de pruebas
Para verificar que las funciones de la librería `maths` funcionan correctamente, creé el archivo `test_math.py`con el siguiente contenido:

```python
import sys, os
sys.path.append(os.getcwd())

from maths import add, subtract, multiply, divide

print("add(2, 3, 5) =", add(2, 3, 5))                   # 10
print("subtract(100, 20, 30, 40) =", subtract(100, 20, 30, 40))  # 10
print("multiply(2, 3, 4) =", multiply(2, 3, 4))         # 24
print("divide(100, 2, 5) =", divide(100, 2, 5))         # 10.0
```

## 18.2 Ejecución de las pruebas
Ejecuté el script con el comando:
```bash
python3 test_math.py
```
El resultado obtenido fue el esperado:
```python
add(2, 3, 5) = 10
subtract(100, 20, 30, 40) = 10
multiply(2, 3, 4) = 24
divide(100, 2, 5) = 10.0
```