from flask import Blueprint, render_template, url_for, request, jsonify, json, Response
from werkzeug.utils import redirect
from sqlalchemy import select

from ..models import User, db, Product

sort = Blueprint('sort', __name__)

# User
@sort.route('/user/sortByUsername', methods=['GET'])
def sort_users_by_username():
    users = User.query.order_by(User.user_username.asc()).all()
    return jsonify(users)

@sort.route('/user/sortByUsername/inOneColumn', methods=['GET'])
def sort_users_by_username_one_column():
    users = User.query.with_entities(User.user_username).order_by(User.user_username.asc()).all()
    return jsonify(users)


# Product
@sort.route('/product/sortByBarcode', methods=['GET'])
def sort_product_by_barcode():
    products = Product.query.order_by(Product.product_barcode.asc()).all()
    return jsonify(products)

# @sort.route('/product/sortByBarcode/inOneColumn', methods=['GET'])
# def sort_product_by_barcode_one_column():
#     products = Product.query.with_entities(Product.product_id).all()
#     return jsonify(products)
