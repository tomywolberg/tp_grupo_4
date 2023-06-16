from db_kiosco import get_db, get_db1, get_db2
from clases_kiosco import Product, Seller, Sales


def insert_product(product_code, name, price, amount, category):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO products (product_code, name, price, amount, category) \
    VALUES ( ?, ?, ?, ?, ?)"
    cursor.execute(statement, [product_code, name, price, amount, category])
    db.commit()
    return True


def update_product(product_code, name, price, amount, category):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE products SET name = ?, price = ?, amount= ?, category= ? \
    WHERE product_code = ?"
    cursor.execute(statement, [name, price, amount, category, product_code])
    db.commit()
    return True


def delete_product(product_code):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM products WHERE product_code = ?"
    cursor.execute(statement, [product_code])
    db.commit()
    return True


def get_by_code(product_code):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT product_code, name, price, amount, category FROM [products] \
    WHERE product_code = ?"
    cursor.execute(statement, [product_code])
    single_product = cursor.fetchone()
    product_code = single_product[0]
    name = single_product[1]
    price = single_product[2]
    amount = single_product[3]
    category = single_product[4]
    products = Product(product_code, name, price, amount, category)
    return products.serialize_details()


def get_products():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT product_code, name, price, amount, category FROM products"
    cursor.execute(query)
    product_list = cursor.fetchall()
    list_of_products = []
    for product in product_list:
        product_code = product[0]
        name = product[1]
        price = product[2]
        amount = product[3]
        category = product[4]
        product_to_add = Product(product_code, name, price, amount, category)
        list_of_products.append(product_to_add)
    return list_of_products


def get_employees():
    db1 = get_db1()
    cursor1 = db1.cursor()
    query1 = "SELECT seller_id, seller_name FROM employees"
    cursor1.execute(query1)
    employees_list = cursor1.fetchall()
    list_of_employees = []
    for employee in employees_list:
        seller_id = employee[0]
        seller_name = employee[1]
        seller_to_add = Seller(seller_id, seller_name)
        list_of_employees.append(seller_to_add)
    return list_of_employees


def sell(sale_code, seller_id, product_code):
    db2 = get_db2()
    cursor2 = db2.cursor()
    statement2 = "INSERT INTO sales (sale_code, seller_id, product_code) VALUES (?,?,?)"
    cursor2.execute(statement2, [sale_code, seller_id, product_code])
    db2.commit()
    return True


def get_sales():
    db2 = get_db2()
    cursor2 = db2.cursor()
    query2 = "SELECT sale_code, seller_id, product_code FROM sales"
    cursor2.execute(query2)
    sales_list = cursor2.fetchall()
    list_of_sales = []
    for sales in sales_list:
        sale_code = sales[0]
        seller_id = sales[1]
        product_code = sales[2]
        sale_to_add = Sales(sale_code, seller_id, product_code)
        list_of_sales.append(sale_to_add)
    return list_of_sales
