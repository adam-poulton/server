from ..models import Product, db
from flask import Blueprint, render_template, url_for, request, jsonify
from werkzeug.utils import redirect
import json
product = Blueprint('products', __name__)

with open("data/products.json") as f:
    # load the test data from the json file
    data = json.load(f)


@product.route('/display')
def get_products():
    return render_template('products.html', Products=Product.query.all())


@product.route('/addProduct')
def add_product():
    entry = Product(product_barcode="steven", product_name="peanut butter", product_brand="kraft")
    db.session.add(entry)
    db.session.commit()
    return redirect(url_for('products.getProducts'))


@product.route("/", methods=['GET'])
def query_all_records():
    """
    Returns all products in the database in json form
    :return: json containing all the products
    """
    return jsonify(data)


@product.route("/", methods=['POST'])
def new_product():
    """
    Create a new product based on the supplied data unless barcode already exists
    :return: json containing the product information of the newly created product
    """
    pass


@product.route("/all", methods=['PUT'])
def update_all_records():
    """
    Updates all products in batch that have had data supplied in the request
    *** FOR DEVELOPMENT & TESTING ONLY ***
    :return: json response indicating success
    """
    return jsonify({"status": "update_all_records"})


@product.route("/", methods=['DELETE'])
def delete_all_records():
    """
    Delete all products in the database
    *** FOR DEVELOPMENT & TESTING ONLY ***
    :return: json response indicating success
    """
    return jsonify({"status": "delete_all_records"})


@product.route("/<barcode>", methods=['GET'])
def get_product(barcode):
    """
    Get details for product with matching barcode or return not found
    :param barcode: barcode of the product
    :return: json response containing product info or not found error
    """
    for item in data:
        if item['barcode'] == barcode:
            return jsonify(item)
    return jsonify({"status": "product not found"})


@product.route("/", methods=['PUT'])
def update_product(barcode):
    """
    Update details for product with matching barcode or return not found
    :param barcode: barcode of the product
    :return: json response containing product info or not found error
    """
    return jsonify({"status": "update_product"})


@product.route("/<barcode>", methods=['DELETE'])
def delete_product(barcode):
    """
    Deletes a product corresponding to a given barcode
    :param barcode: the product barcode
    :return: json response corresponding to success / fail
    """
    return jsonify({"status": "delete_product", "barcode": "{}".format(barcode)})
