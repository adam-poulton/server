from datetime import datetime
from server.database import db_session
from flask import Blueprint, request, jsonify
from server.models import Review, User
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
                session.add(new_feedback)
                session.commit()
            return jsonify({"status": "success", "message": "review created"})
        else:
            return jsonify({"status": "error", "message": "user not found"}), 405
    return jsonify({"status": "error", "message": "user_id missing"}), 405

