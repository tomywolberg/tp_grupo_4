class Product:

    def __init__(self, product_code, name, price, amount, category) -> None:
        self.product_code = product_code
        self.name = name
        self.price = price
        self.amount = amount
        self.category = category

    def serialize(self):
        return {
            'product_code': self.product_code,
            'name': self.name,
            'amount': self.amount,
            'price': self.price
        }

    def serialize_details(self):
        return {
            'product_code': self.product_code,
            'name': self.name,
            'price': self.price,
            'amount': self.amount,
            'category': self.category
        }


class Seller:
    def __init__(self, seller_code, seller_name) -> None:
        self.seller_code = seller_code
        self.seller_name = seller_name

    def serialize1(self):
        return {
            'seller_code': self.seller_code,
            'seller_name': self.seller_name
        }


class Sales:
    def __init__(self, sale_code, seller_id, product_code) -> None:
        self.sale_code = sale_code
        self.seller_id = seller_id
        self.product_code = product_code

    def serialize2(self):
        return {
            'sale_code': self.sale_code,
            'seller_id': self.seller_id,
            'product_code': self.product_code
        }
