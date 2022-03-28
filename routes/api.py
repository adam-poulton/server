from flask import jsonify, Blueprint

from server.routes.products import product
from server.routes.user import user

api = Blueprint('api', __name__)
api.register_blueprint(user, url_prefix='/user')
api.register_blueprint(product, url_prefix='/product')


