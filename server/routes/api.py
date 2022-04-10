from flask import Blueprint
from server.routes.product import product
from server.routes.user import user

api = Blueprint('api', __name__, url_prefix='/api')
api.register_blueprint(product, url_prefix='/product')
api.register_blueprint(user, url_prefix='/user')
