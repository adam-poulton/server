from flask import Blueprint
from server.routes.product import product
from server.routes.user import user
from server.routes.feedback import feedback
from server.routes.favourite import favourite
from server.routes.scan import scan
from server.routes.review import review

api = Blueprint('api', __name__)
api.register_blueprint(product, url_prefix='/product')
api.register_blueprint(user, url_prefix='/user')
api.register_blueprint(favourite, url_prefix='/favourite')
api.register_blueprint(feedback, url_prefix='/feedback')
api.register_blueprint(scan, url_prefix='/scan')
api.register_blueprint(review, url_prefix='/review')