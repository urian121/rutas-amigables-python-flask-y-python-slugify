from flask import Flask, render_template, url_for, abort
from slugify import slugify

# Configuración básica de Flask
app = Flask(__name__)

# Datos en memoria (simulando DB)
PRODUCTS = [
  {"id": 1, "name": "Camiseta Blanca de Algodón", "price": 29.99},
  {"id": 2, "name": "Laptop Gamer RTX 4090", "price": 2499.00},
  {"id": 3, "name": "Auriculares Inalámbricos Bluetooth", "price": 79.5},
]

# Generar slug al arrancar (podrías guardarlo en DB en vez de generarlo cada vez)
for p in PRODUCTS:
  p["slug"] = slugify(p["name"])

# Rutas de la app
@app.route("/")
def index():
  # Mostrar lista de productos con enlaces a /producto/<slug>
  return render_template("index.html", products=PRODUCTS)

# Ruta para mostrar un producto por slug
@app.route("/producto/<slug>")
def producto(slug):
  # Buscar producto por slug
  prod = next((p for p in PRODUCTS if p["slug"] == slug), None)
  if not prod:
      abort(404)
  # Mostrar producto y la URL amigable (la misma que estás usando)
  friendly = url_for("producto", slug=prod["slug"])
  return render_template("product.html", product=prod, friendly_url=friendly)

# Iniciar app
if __name__ == "__main__":
  app.run(debug=True)