from flask import jsonify, Blueprint

from server.routes.products import product
from server.Test.sort import sort


test = Blueprint('test', __name__)
test.register_blueprint(sort, url_prefix='/sort')