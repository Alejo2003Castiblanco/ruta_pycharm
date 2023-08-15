'''Realizamos la instalación de FLask es un framework de python
 para relizar la instalación usamos el siguiente comando python -m pip install flask
 cuando ya quede instalado realizamos importación su modulo llamado Flask.
 Desde flask para poder converitr un objeto en archivo json importamos jsonify '''

from flask import Flask, jsonify, request
from products import products
#ejecutamos flask y le damos una propiedad llaamda name una vez que lo iniciemos esto nos devolvera un objeto llamado app

app = Flask(__name__)


#Aqui estamos testeando que si funciona nuestro servidor y que funciona la ruta de la api para mostrarnos la palabra pong!
@app.route("/ping")
def ping():
    return jsonify({"message": "Pong!"})

#Ya con esta nueva ruta creada lo que hacemos en es un metodo GET para traer información de nuestro archivo products.py
@app.route('/products')
def getProducts():
    return jsonify({"products": products, "message": "Product's list"})

'''Con esta nueva ruta creada de restapi lo que estamos haciendo es que pedimos un producto con su nombre en especifico cuando 
lo encuentre nos trae un arreglo con el nombre del prodcuto ingresado y si no es asi nos dara un mensaje de producto no encontrado'''
@app.route('/products/<string:product_name>')
def getProduct(product_name):
    productsFound = [
        product for product in products if product['name'] == product_name.lower()]
    if (len(productsFound) > 0):
        return jsonify({'product': productsFound[0]})
    return jsonify({'message': 'Product Not found'})

'''Con esta nueva ruta creada de restapi lo que etsamos haciendo es crear datos con un metodo POST desde insomnia'''
@app.route('/products', methods=['POST'])
def addProduct():
    new_product = {
        'name': request.json['name'],
        'price': request.json['price'],
        'quantity': request.json['quantity']
    }
    products.append(new_product)
    return jsonify({'Message': "Product Added Successfully", "products": products})

'''En esta nueva ruta creada de restapi lo que etsamos haciendo es una actualización del producto que nosotros 
deseamos actualizar con un metodo PUT desde insomnia'''

@app.route('/products/<string:product_name>', methods=['PUT'])
def editProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if (len(productsFound) > 0):
        productsFound[0]['name'] = request.json['name']
        productsFound[0]['price'] = request.json['price']
        productsFound[0]['quantity'] = request.json['quantity']
        return jsonify({
            'message': 'Product Updated',
            'product': productsFound[0]
        })
    return jsonify({'message': 'Product Not found'})

'''Con esta nueva ruta creada de restapi lo que haremos es eleminar un prodcuto con el archivo json desde insomnia
con un metodo DELETE'''

@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if len(productsFound) > 0:
        products.remove(productsFound[0])
        return jsonify({
            'message': 'Product Deleted',
            'products': products
        })



#Para inicializar realizamos esta incondicional
if __name__ == '__main__':
    app.run(debug=True, port=5000)
# Para ejecutar nuestro servidor usamos el comando flask --debug run
#Al ejecutarlo nos mostrara 404 not found pero es porque no tenemos ninguna función