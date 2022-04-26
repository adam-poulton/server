from datetime import datetime

from sqlalchemy import desc, asc

from server.database import db_session
from flask import Blueprint, request, jsonify
from server.models import Review, User, Product
from pytz import timezone

review = Blueprint('review', __name__)


@review.route('/new', methods=['POST'])
def new_review():
    """
    Create a new review based on the supplied data
    :return: json containing the newly create review or not found error or missing error
    """
    r_data = request.form
    user_id = r_data.get("user_id")
    product_id = r_data.get("product_id")
    rating = r_data.get("review_rating")
    date = datetime.now(timezone('Australia/Sydney'))  # we define review date locally
    description = r_data.get("review_description")

    if not rating or not description:
        return jsonify({"status": "error", "message": "missing parameter(s)"}), 405

    if not product_id:
        return jsonify({"status": "error", "message": "product_id missing"}), 405

    if user_id:
        match_user = User.query.get(user_id)
        if match_user is not None:
            with db_session() as session:
                new_feedback = Review(
                    user_id=user_id,
                    product_id=product_id,
                    review_rating=rating,
                    review_date=date,
                    review_description=description,
                )
                match_user.user_contribution_score += 5  # Add 5 points to the user contribution
                session.add(new_feedback)
                session.commit()
            return jsonify({"status": "success", "message": "review created"})
        else:
            return jsonify({"status": "error", "message": "user not found"}), 405
    return jsonify({"status": "error", "message": "user_id missing"}), 405


@review.route('/get', methods=['GET'])
def query_all_review():
    """
    Query all reviews in the database in json form or all review from the user if user_id is identified in path
    parameters
    :return: json response containing a list of reviews joined with user table OR not found error
    """
    product_id = request.args.get('product_id')
    if product_id:
        match_user = Product.query.get(product_id)
        if match_user is None:
            return jsonify({"status": "error", "message": "Product not found"}), 405
        with db_session() as session:
            result = session.query(Review, User).join(User).filter(Review.product_id == product_id). \
                order_by(desc(Review.review_date)). \
                all()
            response = []
            for r, u in result:
                d = {
                    "review_rating": r.review_rating,
                    "review_date": r.review_date,
                    "review_description": r.review_description,
                    "pimg_url": u.user_pimg_url,
                    "username": u.user_username,
                }
                response.append(d)
            return jsonify(response)
    else:
        response = []
        with db_session() as session:
            reviews = session.query(Review, User).join(User). \
                order_by(desc(Review.review_date)). \
                all()

            for r, u in reviews:
                d = {
                    "review_rating": r.review_rating,
                    "review_date": r.review_date,
                    "review_description": r.review_description,
                    "pimg_url": u.user_pimg_url,
                    "username": u.user_username,
                }
                response.append(d)
        return jsonify(response)
