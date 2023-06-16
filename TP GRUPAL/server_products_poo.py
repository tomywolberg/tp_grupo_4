from flask import Flask, jsonify, request
import product_controller_poo
from db_kiosco import create_tables, create_tables1, create_tables2, seed_employees, seed_products
from exchange_rate import get_xr

app = Flask(__name__)


@app.route('/products', methods=["GET"])
def get_products():
    products = product_controller_poo.get_products()
    products_list = []
    for product in products:
        elem = product.serialize()
        products_list.append(elem)
    return jsonify(products_list)


@app.route("/product/create", methods=["POST"])
def insert_product():
    product_details = request.get_json()
    product_code = product_details["product_code"]
    name = product_details["name"]
    price = product_details["price"]
    amount = product_details["amount"]
    category = product_details["category"]
    result = product_controller_poo.insert_product(product_code, name, price, amount, category)
    return jsonify(result)


@app.route("/product/modify", methods=["PUT"])
def update_product():
    product_details = request.get_json()
    product_code = product_details["product_code"]
    name = product_details["name"]
    price = product_details["price"]
    amount = product_details["amount"]
    category = product_details["category"]
    result = product_controller_poo.update_product(product_code, name, price, amount, category)
    return jsonify(result)


@app.route("/product/eliminate/<product_code>", methods=["DELETE"])
def delete_product(product_code):
    result = product_controller_poo.delete_product(product_code)
    return jsonify(result)


@app.route("/product/<product_code>", methods=["GET"])
def get_product_by_code(product_code):
    product = product_controller_poo.get_by_code(product_code)
    return jsonify(product)


@app.route('/sales', methods=["GET"])
def get_sales():
    sales = product_controller_poo.get_sales()
    sales_list = []
    for sale in sales:
        elem = sale.serialize2()
        sales_list.append(elem)
    return jsonify(sales_list)


@app.route('/employees', methods=["GET"])
def get_employees():
    employees = product_controller_poo.get_employees()
    employees_list = []
    for employee in employees:
        elem = employee.serialize1()
        employees_list.append(elem)
    return jsonify(employees_list)


@app.route('/sell', methods=["POST"])
def sell():
    product_details = request.get_json()
    sale = product_details["sale_code"]
    seller = product_details["seller_id"]
    product = product_details["product_code"]
    result = product_controller_poo.sell(sale, seller, product)
    return jsonify(result)


@app.route("/products/usd/<product_code>", methods=["GET"])
def get_game_by_id_usd(product_code):
    product = product_controller_poo.get_by_code(product_code)
    xr = get_xr()
    price_usd = product['price'] / xr
    product['price'] = round(price_usd, 2)
    return jsonify(product)


create_tables()
create_tables1()
create_tables2()
seed_employees()
seed_products()
app.run()

if __name__ == '__main__':
    app.run()
