from flask import Blueprint, render_template, request, jsonify
from server.database import db_session
from server.models import Favourite, Product, User

favourite = Blueprint('favourite', __name__)


@favourite.route('/display')
def display_favourites():
    return render_template('favourites.html', Favourites=Favourite.query.all())


@favourite.route('/get', methods=['GET'])
def get_all_favourites():
    user_id = request.args.get('user_id')
    if user_id:
        match_user = User.query.get(user_id)
        if match_user is None:
            return jsonify({"status": "error", "message": "user not found"}), 405
        with db_session() as session:
            favourite_products = session.query(Product)\
                .join(Favourite).filter(Favourite.user_id == user_id).all()
        response = []
        for item in favourite_products:
            d = {'product_id': item.product_id,
                 'product_barcode': item.product_barcode,
                 'product_name': item.product_name,
                 'product_cate': item.product_cate,
                 'product_brand': item.product_brand,
                 'product_price': item.product_price,
                 'product_is_starred': True,
                 'product_nutrition': item.product_nutrition}
            response.append(d)
        return jsonify(response)
    else:
        results = Favourite.query.all()
        return jsonify(results)


@favourite.route('/get/<favourite_id>', methods=['GET'])
def get_favourite(favourite_id):
    match = Favourite.query.get(favourite_id)
    return jsonify(match)


@favourite.route('/add', methods=['POST'])
def add_favourite():
    data = request.form
    user_id = data.get('user_id')
    product_id = data.get('product_id')
    if user_id and product_id:
        with db_session() as session:
            # check that the favourite doesn't already exist
            if not session.query(Favourite).filter_by(user_id=user_id, product_id=product_id).first():
                new_fav = Favourite(user_id=user_id, product_id=product_id)
                session.add(new_fav)
                session.commit()
                return jsonify({"status": "success", "message": "favourite added"})
            else:
                return jsonify({"status": "error", "message": "already a favourite"}), 405
    else:
        return jsonify({"status": "error", "message": "missing parameter(s)"}), 405


@favourite.route('/remove', methods=['POST'])
def remove_favourite():
    data = request.form
    user_id = data.get('user_id')
    product_id = data.get('product_id')
    if user_id and product_id:
        with db_session() as session:
            match = session.query(Favourite).filter_by(user_id=user_id, product_id=product_id).first()
            if match:
                session.delete(match)
                session.commit()
                return jsonify({"status": "success", "message": "favourite removed"})
            else:
                return jsonify({"status": "error", "message": "already a favourite"}), 405
    else:
        return jsonify({"status": "error", "message": "missing parameter(s)"}), 405

