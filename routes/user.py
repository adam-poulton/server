from flask import Blueprint, render_template, url_for, request, jsonify, json
from werkzeug.utils import redirect

from ..models import User, db

user = Blueprint('users', __name__)


@user.route('/display', methods= ['GET'])
def getUsers_inTable():
    """
    Returns all users in the database in html table form, mainly used for development
    """
    return render_template('users.html', Users=User.query.all())


@user.route('/get', methods=['GET'])
def getUsers():
    """
    Returns all users in the database in json form
    """
    users = User.query.all()
    return jsonify(users)


@user.route('/getByEmail/<email>', methods=['GET'])
def getUserByEmail(email):
    """
    Return a matched user in json form with matching email or return not found
    :param email: the user email
    :return: json response containing user info or not found error
    """
    # params = [i for i in request.args.keys()]
    user = User.query.filter_by(user_email=email).first()
    if user:
        return jsonify(user)
    else:
        return jsonify({"message": "user not found"})


@user.route('/add', methods=['POST'])
def addUser():
    """
    Create a new user based on the supplied data
    :return: json containing the user information of the newly created user
    """

    # if bcrypt.hashpw(password, user['password'].encode('utf-8')) == user['password'].encode('utf-8'):
    data = request.form
    username = data['username']
    lname = data['lastname']
    fname = data['firstname']
    email = data['email']
    password = data['password']
    pimg_url = data.get('pimg_url',None)   # we set the pimg_url as nullable field

    user = User(user_username=username, user_firstname=fname, user_lastname=lname, user_email=email, user_password=password, user_contribution_score=0, user_pimg_url=pimg_url)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('api.users.getUsers'))


@user.route('/updatepassword/<email>', methods=['PUT'])
def update_password_by_email(email):
    """
    Update password of user with matching email or return not found
    :param email: the user email
     :return: json containing the user information of the matched user
    """
    user = User.query.filter_by(user_email=email).first()
    if user:
        data = request.form
        password = data['password']
        user.user_password = password
        db.session.commit()
        return jsonify(user)
    else:
        return jsonify({"message": "user not found"})


@user.route('/deleteByEmail/<email>', methods=['DELETE', 'GET'])
def delete(email):
    """
    Deletes a user corresponding to a given email
    :param email: the user email
    :return: json response corresponding to success / fail
    """
    user = User.query.filter_by(user_email=email).first()
    if user:
        db.session.delete(user)
        db.session.commit()
        return redirect(url_for('api.users.getUsers'))
    else:
        return jsonify({"message": "user not found"})


@user.route('/deleteAll', methods=['DELETE', 'GET'])
def deleteAll():
    """
    Delete all users, mainly used for development
    """
    db.session.query(User).delete()
    db.session.commit()
    return redirect(url_for('api.users.getUsers'))

