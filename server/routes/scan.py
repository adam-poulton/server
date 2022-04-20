from flask import Blueprint, render_template, url_for, request, jsonify
from werkzeug.utils import redirect, secure_filename
from pytz import timezone
from datetime import datetime

from server.database import db_session
from server.models import Scan, Product, User, Favourite

scan = Blueprint('scan', __name__)


@scan.route('/get', methods=['GET'])
def get_scan():
    user_id = request.args.get('user_id')
    if user_id:
        match_user = User.query.get(user_id)
        if match_user is None:
            jsonify({"status": "error", "message": "user not found"}), 405
        with db_session() as session:
            favourites = session.query(Favourite.product_id).filter_by(user_id=user_id).all()
            if favourites:
                # unpack all the ids from the returned list of row tuples
                favourites = [item[0] for item in favourites]
            # get the product and scan data combine all into response
            response = []
            for prod, s in session.query(Product, Scan).select_from(Product) \
                    .join(Scan).filter_by(user_id=user_id).order_by(Scan.timestamp.desc()).all():
                d = {'product_id': prod.product_id,
                     'product_barcode': prod.product_barcode,
                     'product_name': prod.product_name,
                     'product_cate': prod.product_cate,
                     'product_brand': prod.product_brand,
                     'product_price': prod.product_price,
                     'product_scan_timestamp': s.timestamp,
                     'product_nutrition': prod.product_nutrition}
                if favourites is not None and prod.product_id in favourites:
                    d['product_is_starred'] = True
                else:
                    d['product_is_starred'] = False
                response.append(d)
            # only return the last 20 scans
            if len(response) > 20:
                response = response[0:20]
            return jsonify(response)


@scan.route('/add', methods=['POST'])
def add_scan():
    user_id = request.form.get('user_id')
    barcode = request.form.get('product_barcode')
    if user_id and barcode:
        with db_session() as session:
            # check that user exists
            match_user = session.query(User).get(user_id)
            if match_user is None:
                return jsonify({"status": "error", "message": "user not found"}), 405
            # check that product exists
            match_product = session.query(Product).filter_by(product_barcode=barcode).first()
            if match_product is None:
                return jsonify({"status": "error", "message": "product not found"}), 405
            # check if previous scan exist for this product and user and delete it if it does
            match_scan = session.query(Scan).filter_by(product_id=match_product.product_id, user_id=user_id).first()
            if match_scan:
                session.delete(match_scan)
            # create the new scan record
            new_scan = Scan(
                product_id=match_product.product_id,
                user_id=user_id,
                timestamp=datetime.now(timezone('Australia/Sydney'))
            )
            session.add(new_scan)
            # commit the changes
            session.commit()
            return jsonify(new_scan)
    else:
        return jsonify({"status": "error", "message": "missing parameter(s)"}), 405
