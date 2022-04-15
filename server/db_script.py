import json
import os

from server.database import db_session
from server.models import Product

basedir = os.path.getcwd()
data = os.path.join(basedir, 'data', 'products.json')


def insert_products():
    with open(data) as f:
        products = json.load(f)

    with db_session() as session:
        for product in products:
            new_product = Product(product_barcode=product['barcode'],
                                  product_name=product['name'],
                                  product_cate=product['category'],
                                  product_brand=product['brand'],
                                  product_nutrition=json.dumps(product['nutrition'])
                                  )
            session.add(new_product)
            session.commit()
