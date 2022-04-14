from flask import Blueprint, render_template, url_for, request, jsonify
from werkzeug.utils import redirect, secure_filename

from server.database import db_session
from server.models import Favourite

favourite = Blueprint('favourite', __name__)


@favourite.route('/display')
def display_favourites():
    return render_template('favourites.html', Favourites=Favourite.query.all())


@favourite.route('/get', methods=['GET'])
def get_all_favourites():
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
                return jsonify(new_fav)
            else:
                return jsonify({"status": "error", "message": "already a favourite"})
    else:
        return jsonify({"status": "error", "message": "missing parameter(s)"})


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
                return jsonify({"status": "error", "message": "already a favourite"})
    else:
        return jsonify({"status": "error", "message": "missing parameter(s)"})

