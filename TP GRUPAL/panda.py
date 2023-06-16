import pandas as pd

productos = [
    {
        'name': 'caramelo',
        'price': 10,
        'amount': 500,
        'category': 'golosina'
    },
    {
        'name': 'chicle',
        'price': 20,
        'amount': 400,
        'category': 'golosina'
    },
    {
        'name': 'coca cola',
        'price': 50,
        'amount': 300,
        'category': 'gaseosa'
    },
    {
        'name': 'alfajor',
        'price': 70,
        'amount': 350,
        'category': 'golosina'
    },
    {
        'name': 'fanta',
        'price': 45,
        'amount': 150,
        'category': 'gaseosa'
    },
]

prod = pd.DataFrame(productos)

print(prod.describe())
