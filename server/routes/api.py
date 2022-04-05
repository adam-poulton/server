from flask import jsonify, Blueprint

from server.routes.products import product
from server.routes.user import user
from server.routes.starredProducts import starredProduct

api = Blueprint('api', __name__)
api.register_blueprint(user, url_prefix='/user')
api.register_blueprint(product, url_prefix='/product')
# api.register_blueprint(starredProduct, url_prefix='/star')