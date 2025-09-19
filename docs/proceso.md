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

**Acción:** En la carpeta `docs/` creé un nuevo archivo:

```text
proceso.md
```

**Resultado:** Ahora tengo dos páginas en la documentación: `index.md` y `proceso.md`.

---

## 4. Configuración de la navegación

**Archivo editado:** `mkdocs.yml`

**Configuración añadida:**

```yaml
site_name: Documentación de Ale

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

## 6. Compilación del sitio (sin publicación)

**Comando usado:**
```bash
mkdocs build
