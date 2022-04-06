import json
import re
import time
from pathlib import Path

from flask import Blueprint, render_template, url_for, request, jsonify
from werkzeug.utils import redirect, secure_filename

from ..models import Favourite, db, Product


starredProduct = Blueprint('favourites', __name__)


@starredProduct.route('/display')
def display_products():
    return render_template('favourites.html', Favourites=Favourite.query.all())


@starredProduct.route('/get', methods='GET')
def get_favourite():
    favourite = Favourite.query.all()
    return jsonify(favourite)


@starredProduct.route('/add/<product_id>', methods='POST')
def add_favourite(product_id):
    favourite = Favourite(product_id = product_id)
    db.session.add(favourite)
    return redirect(url_for('api.starProducts.get_favourite', favourite_id=favourite.favourite_id))


@starredProduct.route('/productDetails')
def get_products():
    starredProducts = Favourite.query.all()


