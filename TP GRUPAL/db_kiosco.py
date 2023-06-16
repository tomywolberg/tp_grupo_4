import sqlite3

DATABASE_NAME = "atributes.db"


def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def create_tables():
    tables = [
        """CREATE TABLE IF NOT EXISTS products(
                product_code INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                price REAL NOT NULL,
                amount INTEGER NOT NULL,
                category TEXT NOT NULL
            )
            """
    ]
    db = get_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)


def seed_products():
    queries = ["INSERT OR IGNORE INTO products (product_code, name, price, amount, category) VALUES (1, 'caramelo' , 50, 100, 'golosina')",
               "INSERT OR IGNORE INTO products (product_code, name, price, amount, category) VALUES (2, 'chicle' , 60, 150, 'golosina')",
               "INSERT OR IGNORE INTO products (product_code, name, price, amount, category) VALUES (3, 'coca cola' , 100, 50, 'gaseosa')",
               "INSERT OR IGNORE INTO products (product_code, name, price, amount, category) VALUES (4, 'fanta' , 95, 55, 'gaseosa')",
               ]
    db = get_db()
    cursor = db.cursor()
    for query in queries:
        cursor.execute(query)
    db.commit()


DATABASE_NAME1 = "seller_atributes.db"


def get_db1():
    conn = sqlite3.connect(DATABASE_NAME1)
    return conn


def create_tables1():
    tables1 = [
        """CREATE TABLE IF NOT EXISTS employees(
                seller_id INTEGER PRIMARY KEY,
                seller_name TEXT NOT NULL
            )
            """
    ]
    db1 = get_db1()
    cursor1 = db1.cursor()
    for table1 in tables1:
        cursor1.execute(table1)


def seed_employees():
    queries = ["INSERT OR IGNORE INTO employees (seller_id, seller_name) VALUES (1, 'Pablo')",
               "INSERT OR IGNORE INTO employees (seller_id, seller_name) VALUES (2, 'Jorge')",
               "INSERT OR IGNORE INTO employees (seller_id, seller_name) VALUES (3, 'Manu')"]
    db1 = get_db1()
    cursor1 = db1.cursor()
    for query in queries:
        cursor1.execute(query)
    db1.commit()


DATABASE_NAME2 = "sales_atributes.db"


def get_db2():
    conn = sqlite3.connect(DATABASE_NAME2)
    return conn


def create_tables2():
    tables2 = [
        """CREATE TABLE IF NOT EXISTS sales(
                sale_code INTEGER PRIMARY KEY,
                seller_id INTEGER NOT NULL,
                product_code INTEGER NOT NULL,
                CONSTRAINT seller1 FOREIGN KEY (seller_id)
                REFERENCES seller (seller_id)
                CONSTRAINT product1 FOREIGN KEY (product_code)
                REFERENCES products (product_code)
            )
            """
    ]
    db2 = get_db2()
    cursor2 = db2.cursor()
    for table2 in tables2:
        cursor2.execute(table2)
