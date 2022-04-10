import json
import re
import time
from pathlib import Path

from flask import Blueprint, render_template, url_for, request, jsonify
from werkzeug.utils import redirect, secure_filename

from ..models import Favourite, db


favourites = Blueprint('favourites', __name__)


@favourites.route('/display')
def display_products():
    return render_template('favourites.html', Favourites=Favourite.query.all())


@favourites.route('/get', methods='GET')
def get_all_favourites():
    favourites = Favourite.query.all()
    return jsonify(favourites)


@favourites.route('/get/<favourite_id>', methods='GET')
def get_favourite(favourite_id):
    favourite = Favourite.query.get(favourite_id)
    return jsonify(favourite)


@favourites.route('/add', methods='POST')
def add_favourite():
    data = request.form
    user_id = data.get('user_id')
    product_id = data.get('product_id')
    if user_id and product_id:
        if not Favourite.query.filter_by(user_id=user_id, product_id=product_id).first():
            favourite = Favourite(user_id=user_id, product_id=product_id)
            db.session.add(favourite)
            return redirect(url_for('api.starProducts.get_favourite', favourite_id=favourite.favourite_id))
        return jsonify({"status": "error", "message": "missing parameter(s)"})
    else:
        return jsonify({"status": "error", "message": "missing parameter(s)"})



