import json
import re
import time
from pathlib import Path

from flask import Blueprint, render_template, url_for, request, jsonify
from werkzeug.utils import redirect, secure_filename

from ..models import Product, db

product = Blueprint('products', __name__)

data_folder = Path("data/").resolve()
image_folder = data_folder / "images/"
data_file = data_folder / "products.json"
with open(data_file) as f:
    # load the test data from the json file
    product_test_data = json.load(f)


@product.route('/display')
def get_products():
    return render_template('products.html', Products=Product.query.all())


@product.route("/get", methods=['GET'])
def query_all_records():
    """
    Returns all products in the database in json form
    :return: json containing all the products
    """
    return jsonify(product_test_data)


@product.route("/get/<barcode>", methods=['GET'])
def get_product(barcode):
    """
    Get details for product with matching barcode or return not found
    :param barcode: barcode of the product
    :return: json response containing product info or not found error
    """
    for item in product_test_data:
        if item['barcode'] == barcode:
            return jsonify(item)

    prod = Product.query.filter_by(barcode=barcode).first()
    if prod is not None:
        return jsonify(prod)

    return jsonify({"status": "product not found"})


@product.route("/new", methods=['POST'])
def new_product():
    """
    Create a new product based on the supplied data unless barcode already exists
    :return: json containing the product information of the newly created product
    """
    # parse the request data
    r_data = request.args
    name = r_data.get('name')
    brand = r_data.get('brand')
    category = r_data.get('category')
    barcode = r_data.get('barcode')

    # check to ensure that there are no illegal characters in the barcode
    if not valid_barcode(barcode):
        return jsonify({"error": "invalid barcode"})

    # check to ensure record for barcode does not exist in database
    match = Product.query.filter_by(barcode=barcode).first()
    if match is None:
        # capture the image files
        files_ids = list(request.files)
        for file_id in files_ids:
            image_file = request.files[file_id]
            filename = secure_filename(image_file.filename)
            time_str = time.strftime("%Y%m%d-%H%M%S")
            image_file.save("{}{}_{}".format(image_folder, time_str, filename))
        # create the new database object
        new_prod = Product(
            product_name=name,
            product_brand=brand,
            product_cate=category,
            product_barcode=barcode)

        db.session.add(new_prod)
        db.session.commit()
        return redirect(url_for('api.products.get_product', barcode=barcode))
    else:
        return jsonify({"error": "barcode already exists"})


@product.route("/update", methods=['PUT'])
def update_product(barcode):
    """
    Update details for product with matching barcode or return not found
    :param barcode: barcode of the product
    :return: json response containing product info or not found error
    """
    # parse the request data
    r_data = request.args
    name = r_data.get('name')
    brand = r_data.get('brand')
    category = r_data.get('category')
    barcode = r_data.get('barcode')

    return jsonify({"status": "update_product"})


@product.route("/delete", methods=['DELETE'])
def delete_product(barcode):
    """
    Deletes a product corresponding to a given barcode
    :param barcode: the product barcode
    :return: json response corresponding to success / fail
    """
    return jsonify({"status": "delete_product", "barcode": "{}".format(barcode)})


def valid_barcode(barcode):
    """
    Validates a barcode submitted to the server
    :param barcode:
    :return: True if the barcode string contains only numerical characters and is non-empty
                otherwise, False
    """
    if len(barcode) == 0:
        return False
    barcode_num = re.sub('[^0-9]', '', barcode)
    return 0 < len(barcode_num) == len(barcode)
