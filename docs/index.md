# Librería Matemática

Este proyecto incluye una librería matemática llamada **`maths`** desarrollada como parte de la práctica.  
La librería ha sido integrada en el repositorio y documentada con MkDocs.

---

## Funciones disponibles

La librería contiene cuatro funciones principales, todas ellas capaces de recibir un número indefinido de argumentos gracias al uso de `*args`:

- **`add(*args)`** → Devuelve la suma de todos los números.
- **`subtract(*args)`** → Resta los números de forma secuencial.
- **`multiply(*args)`** → Calcula el producto de los números.
- **`divide(*args)`** → Realiza divisiones de manera secuencial (con control de división entre cero).

---

## Ejemplos de uso

```python
from maths import add, subtract, multiply, divide

print(add(2, 3, 5))              # 10
print(subtract(100, 20, 30, 40)) # 10
print(multiply(2, 3, 4))         # 24
print(divide(100, 2, 5))         # 10.0
```

## Estructura de la librería

```bash
maths/
├── __init__.py
├── add.py
├── subtract.py
├── multiply.py
└── divide.py
```