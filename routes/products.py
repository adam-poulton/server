from flask import Blueprint, render_template, url_for
from werkzeug.utils import redirect
import json
product = Blueprint('products', __name__)
from ..models import Product, db


@product.route("/barcode/<barcode_id>")
def barcode(barcode_id):
    return json.dumps({'barcode': barcode_id,
                       'name': 'peanut butter',
                       'brand': 'kraft'})


@product.route('/')
def getProducts():
    return render_template('products.html', Products=Product.query.all())

@product.route('/addProduct')
def addUser():
    product = Product(product_barcode ="steven",product_name = "peanut butter",product_brand="kraft")
    db.session.add(product)
    db.session.commit()
    return redirect(url_for('products.getProducts'))