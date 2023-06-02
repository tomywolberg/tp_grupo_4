from flask import Flask, jsonify, request

app = Flask(__name__)

productos = [
    {'producto': 'caramelo', 'stock': 1000, 'precio': 5},
    {'producto': 'chicle', 'stock': 700, 'precio': 4},
    {'producto': 'chupetin', 'stock': 500, 'precio': 7},
    {'producto': 'cigarrillos', 'stock': 450, 'precio': 10},
]


@app.route('/productos', methods=['GET'])
def productosGet():
    return jsonify({'productos': productos})

@app.route('/productos/<producto>', methods=['GET'])
def productosGetUno(producto):
    for indice, p in enumerate(productos):
        if p['producto'] == producto:
            return jsonify({'productos':productos[indice]})
    return 'error'



@app.route('/productos', methods=['POST'])
def productosPost():
    body = request.json
    print(body)
    producto = body['producto']
    stock = body['stock']
    precio = body['precio']

    newProd = {'producto': producto, 'stock': stock, 'precio': precio}
    productos.append(newProd)

    return jsonify({'productos': productos})


@app.route('/productos/<producto>/operacion/<op>', methods=['PUT'])
def productoPutUpdatePorVenta(producto, op):
    for indice, p in enumerate(productos):
        if p['producto'] == producto:
            if op == 'venta':
                p['stock'] = p['stock'] - 1
            if op == 'compra':
                p['stock'] = p['stock'] + 1

    return jsonify({'productos': productos})


@app.route('/productos/<producto>/<precio>', methods=['PUT'])
def productoPutUpdatePrecio(producto, precio):
    for indice, p in enumerate(productos):
        if p['producto'] == producto:
            p['precio'] = precio

    return jsonify({'productos': productos})


@app.route('/productos/<producto>', methods=['DELETE'])
def productoDelete(producto):
    for indice, p in enumerate(productos):
        if p['producto'] == producto:
            productos[indice: indice + 1] = []
    return jsonify({'productos': productos})


if __name__ == '__main__':
    app.run()
