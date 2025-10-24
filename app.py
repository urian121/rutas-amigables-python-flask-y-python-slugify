from flask import Flask, render_template, url_for, abort
from slugify import slugify

# Configuración básica de Flask
app = Flask(__name__)

# Datos en memoria (simulando DB)
PRODUCTS = [
  {"id": 1, "name": "Camiseta Blanca de Algodón", "price": 29.99},
  {"id": 2, "name": "Laptop Gamer RTX 4090", "price": 2499.00},
  {"id": 3, "name": "Auriculares Inalámbricos Bluetooth", "price": 79.5},
  {"id": 4, "name": "Smartphone Samsung Galaxy S24", "price": 899.99},
  {"id": 5, "name": "Tablet iPad Pro 12.9 pulgadas", "price": 1299.00},
  {"id": 6, "name": "Smartwatch Apple Watch Series 9", "price": 399.00},
  {"id": 7, "name": "Cámara Canon EOS R5", "price": 3899.00},
  {"id": 8, "name": "Altavoz Bluetooth JBL Charge 5", "price": 149.99},
  {"id": 9, "name": "Monitor Gaming 4K 27 pulgadas", "price": 599.00},
  {"id": 10, "name": "Teclado Mecánico RGB Gaming", "price": 89.99},
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