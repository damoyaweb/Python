from flask import Flask, jsonify, request



app = Flask(__name__)

from products import products

@app.route('/ping')
def ping():
    return jsonify({
        "message": "Funciona!!!"
    })

@app.route('/products')
def getProducts():
    return jsonify({"products": products})

@app.route('/products/<int:product_id>')
def getProduct(product_id):
    productFind = [product for product in products if product['id'] == product_id]
    print(product_id)
    if (len(productFind) > 0):
        return jsonify({"product": productFind[0]})
    else:
        return jsonify({"message": "El Producto no se encuentra"})

@app.route('/products', methods=['POST'])
def addProduct():
    new_product = {
        "id": request.json['id'],
		"name": request.json['name'],
		"price": request.json['price'],
		"quantity": request.json['quantity']
    }
    products.append(new_product)
    return jsonify({"mesasge":"Producto Agregado Correctamente","products": products})
@app.route('/products/<int:product_id>', methods=['PUT'])
def putProduct(product_id):
    productFind = [product for product in products if product['id']== product_id]
    if (len(productFind) > 0):
        productFind[0]['name'] = request.json['name']
        productFind[0]['price'] = request.json['price']
        productFind[0]['quantity'] = request.json['quantity']
        return jsonify({
            "message": "Producto Actualizado",
            "product": productFind[0]
        })
    else:
        return jsonify({
            "message": "Producto no Encontrado"
        })
@app.route('/products/<int:product_id>', methods=['DELETE'])
def deleteProduct(product_id):
    productFind = [product for product in products if product['id'] == product_id]
    if (len(productFind)>0):
        products.remove(productFind[0])
        return jsonify({
            "messange": "producto Eliminado",
            "product": products
        })
    else:
        return jsonify({
            "messange": "producto no Encontrado"
        })
if __name__ == '__main__':
    app.run(debug=True, port=4000)