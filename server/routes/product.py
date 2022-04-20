import re
from flask import Blueprint, render_template, url_for, request, jsonify
from werkzeug.utils import redirect, secure_filename

from server.database import db_session
from server.models import Product, Favourite, User

product = Blueprint('products', __name__)


@product.route('/display')
def get_products():
    return render_template('products.html', Products=Product.query.all())


@product.route("/get", methods=['GET'])
def query_all_records():
    """
    Returns all products in the database in json form
    :return: json containing all the products
    """
    user_id = request.args.get('user_id')
    products = Product.query.all()
    if user_id:
        match_user = User.query.get(user_id)
        if match_user is None:
            return jsonify({"status": "error", "message": "user not found"}), 405
        with db_session() as session:
            favourites = session.query(Favourite.product_id).filter_by(user_id=user_id).all()
            if favourites:
                # unpack all the ids from the returned list of row tuples
                favourites = [item[0] for item in favourites]
        response = []
        # iterate over the products and insert the is_starred value
        # TODO: implement this kind of serialisation using Marshmallow
        for item in products:
            d = {'product_id': item.product_id,
                 'product_barcode': item.product_barcode,
                 'product_name': item.product_name,
                 'product_cate': item.product_cate,
                 'product_brand': item.product_brand,
                 'product_price': item.product_price,
                 'product_nutrition': item.product_nutrition}
            if favourites is not None and item.product_id in favourites:
                d['product_is_starred'] = True
            else:
                d['product_is_starred'] = False
            response.append(d)
        return jsonify(response)
    else:
        return jsonify(products)


@product.route("/get/<barcode>", methods=['GET'])
def get_product(barcode):
    """
    Get details for product with matching barcode or return not found
    :param barcode: barcode of the product
    :return: json response containing product info or not found error
    """
    user_id = request.args.get('user_id')
    prod = Product.query.filter_by(product_barcode=barcode).first()
    if prod is None:
        return jsonify({"status": "error", "message": "product not found"}), 405
    elif user_id:
        match_user = User.query.get(user_id)
        if match_user is None:
            return jsonify({"status": "error", "message": "user not found"}), 405
        with db_session() as session:
            favourites = session.query(Favourite.product_id).filter_by(user_id=user_id).all()
            if favourites:
                # unpack all the ids from the returned list of row tuples
                favourites = [item[0] for item in favourites]
        # iterate over the products and insert the is_starred value
        # TODO: implement this kind of serialisation using Marshmallow
        d = {'product_id': prod.product_id,
             'product_barcode': prod.product_barcode,
             'product_name': prod.product_name,
             'product_cate': prod.product_cate,
             'product_brand': prod.product_brand,
             'product_price': prod.product_price,
             'product_nutrition': prod.product_nutrition}
        if favourites is not None and prod.product_id in favourites:
            d['product_is_starred'] = True
        else:
            d['product_is_starred'] = False
        return jsonify(d)
    else:
        return jsonify(prod)


@product.route("/new", methods=['POST'])
def new_product():
    """
    Create a new product based on the supplied data unless barcode already exists
    :return: json containing the product information of the newly created product
    """
    # parse the request data
    r_data = request.form
    name = r_data.get('name')
    brand = r_data.get('brand')
    category = r_data.get('category')
    barcode = r_data.get('barcode')
    nutrition = r_data.get('nutrition')
    price = r_data.get('price', 0)

    # check to ensure that there are no illegal characters in the barcode
    if not valid_barcode(barcode):
        return jsonify({"status": "error", "message": "invalid barcode"}), 405

    # check to ensure record for barcode does not exist in database
    match = Product.query.filter_by(product_barcode=barcode).first()
    if match is None:
        with db_session() as session:
            new_prod = Product(
                product_name=name,
                product_brand=brand,
                product_cate=category,
                product_barcode=barcode,
                product_price=price,
                product_nutrition=nutrition)
            session.add(new_prod)
            session.commit()

            return redirect(url_for('api.products.get_product', barcode=barcode))
    else:
        return jsonify({"status": "error", "message": "barcode already exists"})


@product.route("/update", methods=['PUT'])
def update_product():
    """
    Update details for product with matching barcode or return not found
    :return: json response containing product info or not found error
    """
    # parse the request data
    r_data = request.form
    name = r_data.get('name')
    brand = r_data.get('brand')
    category = r_data.get('category')
    barcode = r_data.get('barcode')
    nutrition = r_data.get('nutrition')
    price = r_data.get('price')

    if barcode is None:
        return jsonify({"status": "error", "message": "barcode missing"}), 405

    with db_session() as session:

        updated_product = session.query(Product).filter_by(product_barcode=barcode).first()

        if updated_product is None:
            return jsonify({"status": "error", "message": "product not found"}), 404

        if name is not None:
            updated_product.product_name = name
        if brand is not None:
            updated_product.product_brand = brand
        if category is not None:
            updated_product.product_cate = category
        if brand is not None:
            updated_product.product_brand = brand
        if price is not None:
            updated_product.product_price = price
        if nutrition is not None:
            updated_product.product_nutrition = nutrition

        session.commit()

        return redirect(url_for('api.products.get_product',
                                barcode=updated_product.product_barcode))


@product.route("/delete/<product_id>", methods=['DELETE'])
def delete_product(product_id=None):
    """
    Delete a product corresponding to a given id
    :return: json response corresponding to success / fail
    """
    if product_id is None:
        return jsonify({"status": "error", "message": "product_id missing"}), 405
    with db_session() as session:
        _product = session.query(Product).get(product_id)
        if not _product:
            return jsonify({"status": "error", "message": "product not found"}), 405

        session.delete(_product)
        session.commit()

        return jsonify({"status": "success", "message": "product deleted"})


@product.route("/similar/<product_id>", methods=['GET'])
def get_similar_product(product_id=None):
    """
    Return a list of products in the same category of the product_id parameter
    :return: json containing a list of products with information containing is_starred attribute
             or json with response corresponding to parameter missing / not found
    """
    user_id = request.args.get('user_id')
    if user_id is None:
        return jsonify({"status": "error", "message": "user_id missing"}), 405
    else:
        # Get the specific user's starred products

        match_user = User.query.get(user_id)
        if match_user is None:
            return jsonify({"status": "error", "message": "user not found"}), 404
        with db_session() as session:
            favourites = session.query(Favourite.product_id).filter_by(user_id=user_id).all()
            if favourites is not None:
                # unpack all the ids from the returned list of row tuples
                favourites = [item[0] for item in favourites]

    if product_id is None:
        return jsonify({"status": "error", "message": "product_id missing"}), 405

    with db_session() as session:
        _product = session.query(Product).get(product_id)
        if not _product:
            return jsonify({"status": "error", "message": "product not found"}), 405

        similar_products = session.query(Product).filter_by(product_cate=_product.product_cate).all()

        response = []  # the response is a list of product with info containing is_starred attribute

        # Iterate over the products and insert the is_starred value
        # TODO: implement this kind of serialisation using Marshmallow
        for item in similar_products:
            d = {'product_id': item.product_id,
                 'product_barcode': item.product_barcode,
                 'product_name': item.product_name,
                 'product_cate': item.product_cate,
                 'product_brand': item.product_brand,
                 'product_price': item.product_price,
                 'product_nutrition': item.product_nutrition}
            if favourites is not None and item.product_id in favourites:
                d['product_is_starred'] = True
            else:
                d['product_is_starred'] = False
            response.append(d)
        return jsonify(response)


def valid_barcode(barcode):
    """
    Validates a barcode submitted to the server
    :param barcode: the barcode string to check
    :return: True if the barcode string contains only numerical characters and is non-empty
                otherwise, False
    """
    if len(barcode) == 0:
        return False
    barcode_num = re.sub('[^0-9]', '', barcode)
    return 0 < len(barcode_num) == len(barcode)
