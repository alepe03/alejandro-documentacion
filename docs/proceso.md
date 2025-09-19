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
