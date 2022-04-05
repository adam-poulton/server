import json
import re
import time
from pathlib import Path

from flask import Blueprint, render_template, url_for, request, jsonify
from werkzeug.utils import redirect, secure_filename

from ..models import Starred_Product, db, Product


starredProduct = Blueprint('starProducts', __name__)


@starredProduct.route('/display')
def display_products():
    return render_template('star_products.html', Starred_Products=Starred_Product.query.all())

@starredProduct.route('/get', methods='GET')
def get_star_roducts():
    starredProducts = Starred_Product.query.all()
    return jsonify(starredProducts)

@starredProduct.route('/add/<product_id>', methods='POST')
def add_star(product_id):
    starredProducts = Starred_Product(product_id = product_id)
    db.session.add(starredProducts)
    return redirect(url_for('api.starProducts.get_star_roducts'))


@starredProduct.route('/productDetailes')
def get_products():
    starredProducts = Starred_Product.query.all()


