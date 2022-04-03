import json
import re
import time
from pathlib import Path

from flask import Blueprint, render_template, url_for, request, jsonify
from werkzeug.utils import redirect, secure_filename

from ..models import Starred_Product, db


starredProduct = Blueprint('starProducts', __name__)


@starredProduct.route('/display')
def display_products():
    return render_template('star_products.html', Starred_Products=Starred_Product.query.all())

@starredProduct.route('/get')
def get_products():
    starredProducts = Starred_Product.query.all()
    return jsonify(starredProducts)



