from flask import Blueprint
from server.routes.product import product
from server.routes.user import user
from server.routes.feedback import feedback
from server.routes.favourite import favourite

api = Blueprint('api', __name__)
api.register_blueprint(product, url_prefix='/product')
api.register_blueprint(user, url_prefix='/user')
api.register_blueprint(favourite, url_prefix='/favourite')
api.register_blueprint(feedback, url_prefix='/feedback')
