from flask import Blueprint, render_template, url_for, request
from werkzeug.utils import redirect
import json
product = Blueprint('products', __name__)
from ..models import Product, db


@product.route("/new", methods=['PUT'])
def new_product():
    """
    Create a new product based on the supplied data unless barcode already exists
    :return: json containing the
    """



@product.route('/')
def getProducts():
    return render_template('products.html', Products=Product.query.all())

@product.route('/addProduct')
def addUser():
    product = Product(product_barcode ="steven",product_name = "peanut butter",product_brand="kraft")
    db.session.add(product)
    db.session.commit()
    return redirect(url_for('products.getProducts'))