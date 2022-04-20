from datetime import datetime
from werkzeug.utils import redirect
from server.database import db_session
from flask import Blueprint, render_template, url_for, request, jsonify
from server.models import Feedback, User
import pytz

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
    now = datetime.now(pytz.timezone('Australia/Sydney')) # we define written date of feedback inside server
    # fdate = now.strftime("%Y/%m/%d-%H:%M:%S")
    r_data = request.form
    user_id = r_data.get("user_id")
    rating = r_data.get("rating")
    description = r_data.get("description")

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
                session.add(new_feedback)
                session.commit()
            return redirect(url_for('api.feedback.query_all_feedback'))
    return jsonify({"status": "error", "message": "user not found"})
