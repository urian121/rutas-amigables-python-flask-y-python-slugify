# Rutas Amigables con Flask

Proyecto que demuestra la implementación de URLs amigables (slugs) en una aplicación Flask.

![Resultado](https://raw.githubusercontent.com/urian121/imagenes-proyectos-github/refs/heads/master/rutas-amigables-python-flask.png)


## Características

- **URLs amigables** usando la librería `python-slugify`
- **Diseño moderno** con Bootstrap 5
- **Plantillas con herencia** usando Jinja2
- **Navegación responsiva** con navbar
- **10 productos de ejemplo** con diferentes categorías

## Estructura del Proyecto

```
├── app.py                 # Aplicación principal Flask
├── templates/
│   ├── base.html         # Plantilla base con navegación y footer
│   ├── index.html        # Lista de productos
│   └── product.html      # Detalle de producto
└── env/                  # Entorno virtual Python
```

## Instalación

1. **Activar entorno virtual**:
   ```bash
   source env/bin/activate
   ```

2. **Instalar dependencias**:
   ```bash
   pip install flask python-slugify
   ```

3. **Ejecutar aplicación**:
   ```bash
   python app.py
   ```

4. **Abrir en navegador**: `http://localhost:5000`

## Funcionalidades

### URLs Amigables
- `/producto/camiseta-blanca-de-algodon` en lugar de `/producto/1`
- Generación automática de slugs desde nombres de productos
- Mejor SEO y experiencia de usuario

### Diseño
- Bootstrap 5 con iconos
- Diseño responsivo para móviles
- Navegación con estado activo
- Footer común en todas las páginas

### Productos
- 10 productos de ejemplo
- Categorías: tecnología, gaming, fotografía, audio
- Precios desde $29.99 hasta $3,899.00

## Tecnologías

- **Python 3.12**
- **Flask 3.1.2**
- **Bootstrap 5.3.2**
- **python-slugify 8.0.4**
- **Jinja2** para plantillas

## Rutas

- `/` - Lista de productos
- `/producto/<slug>` - Detalle de producto por slug
