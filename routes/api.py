from flask import jsonify, Blueprint

api = Blueprint('api', __name__)


@api.route("/products", methods=['POST'])
def new_product():
    """
    Create a new product based on the supplied data unless barcode already exists
    :return: json containing the
    """
    pass


@api.route("/products", methods=['GET'])
def query_all_records():
    """
    Returns all products in the database in json form
    :return: json containing all the products
    """
    return jsonify({"status": "query_all_records"})


@api.route("/products", methods=['PUT'])
def update_all_records():
    """
    Updates all products in batch that have had data supplied in the request
    *** FOR DEVELOPMENT & TESTING ONLY ***
    :return: json response indicating success
    """
    pass


@api.route("/products", methods=['DELETE'])
def delete_all_records():
    """
    Delete all products in the database
    *** FOR DEVELOPMENT & TESTING ONLY ***
    :return: json response indicating success
    """
    pass


@api.route("/products/<barcode>", methods=['GET'])
def get_product(barcode):
    """
    Get details for product with matching barcode or return not found
    :param barcode: barcode of the product
    :return: json response containing product info or not found error
    """
    pass


@api.route("/products/<barcode>", methods=['PUT'])
def update_product(barcode):
    """
    Update details for product with matching barcode or return not found
    :param barcode: barcode of the product
    :return: json response containing product info or not found error
    """
    pass


@api.route("/products/<barcode>", methods=['DELETE'])
def delete_product(barcode):
    """
    Deletes a product corresponding to a given barcode
    :param barcode: the product barcode
    :return: json response corresponding to success / fail
    """
    pass

