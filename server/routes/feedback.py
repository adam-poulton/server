from datetime import datetime
from server.database import db_session
from flask import Blueprint, request, jsonify
from server.models import Feedback, User
from pytz import timezone

feedback = Blueprint('feedback', __name__)


@feedback.route("/get", methods=['GET'])
def query_all_feedback():
    """
    Returns all feedback in the database in json form
    :return: json containing all the feedback
    """
    user_id = request.args.get('user_id')
    feedbacks = Feedback.query.all()
    if user_id:
        match_user = User.query.get(user_id)
        if match_user is not None:
            fb = Feedback.query.filter_by(user_id=user_id).all()
            if fb is not None:
                return jsonify(fb)
        else:
            return jsonify({"status": "error", "message": "user not found"})

    return jsonify(feedbacks)


@feedback.route("/new", methods=['POST'])
def new_feedback():
    """
    Create a new feedback based on the supplied data
    :return: json containing the feedback description of the newly created feedback
    """
    now = datetime.now(timezone('Australia/Sydney')) # we define written date of feedback locally
    # fdate = now.strftime("%Y/%m/%d-%H:%M:%S")
    r_data = request.form
    user_id = r_data.get("user_id")
    rating = r_data.get("feedback_rating")
    description = r_data.get("feedback_description")

    if not rating or not description:
        return jsonify({"status": "error", "message": "missing parameter(s)"}), 405
    if user_id:
        match_user = User.query.get(user_id)
        if match_user is not None:
            with db_session() as session:
                new_feedback = Feedback(
                    user_id=user_id,
                    feedback_description=description,
                    feedback_date=now,
                    feedback_rating=rating,
                )

                match_user.user_contribution_score += 5   # Add 5 points to the user contribution
                session.add(new_feedback)
                session.commit()
            return jsonify({"status": "success", "message": "feedback created"})
        else:
            return jsonify({"status": "error", "message": "user not found"}), 405
    return jsonify({"status": "error", "message": "user_id missing"}), 405
