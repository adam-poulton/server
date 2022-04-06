from flask import jsonify, Blueprint

from server.routes.products import product
from server.routes.user import user
from server.routes.favourite import favourites

api = Blueprint('api', __name__)
api.register_blueprint(user, url_prefix='/user')
api.register_blueprint(product, url_prefix='/product')
api.register_blueprint(favourites, url_prefix='/favourite')