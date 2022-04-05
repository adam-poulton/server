from flask import Blueprint, render_template, url_for, request, jsonify, json
from werkzeug.utils import redirect

from ..models import User, db

user = Blueprint('users', __name__)


@user.route('/display', methods=['GET'])
def get_users_display():
    """
    Returns all users in the database in html table form, mainly used for development
    """
    return render_template('users.html', Users=User.query.all())


@user.route('/get', methods=['GET'])
def get_users():
    """
    Returns all users in the database in json form
    """
    users = User.query.all()
    return jsonify(users)


@user.route('/get/<user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user_match = User.query.get(user_id)
    return jsonify(user_match)


@user.route('/getByEmail/<email>', methods=['GET'])
def get_user_by_email(email):
    """
    Return a matched user in json form with matching email or return not found
    :param email: the user email
    :return: json response containing user info or not found error
    """
    # params = [i for i in request.args.keys()]
    user_match = User.query.filter_by(user_email=email).first()
    return jsonify(user_match)


@user.route('/getByUsername/<username>', methods=['GET'])
def get_user_by_username(username):
    """
    Return a matched user in json form with matching email or return not found
    :param username: the user username
    :return: json response containing user info or not found error
    """
    # params = [i for i in request.args.keys()]
    user_match = User.query.filter_by(user_username=username).first()
    return jsonify(user_match)


@user.route('/getByUsername/<username>', methods=['GET'])
def get_user_by_username(username):
    """
    Return a matched user in json form with matching email or return not found
    :param username: the user username
    :return: json response containing user info or not found error
    """
    # params = [i for i in request.args.keys()]
    user_match = User.query.filter_by(user_username=username).first()
    return jsonify(user_match)


@user.route('/getBy/<login>', methods=['GET'])
def get_user_by(login):
    """
    Return a matched user in json form with matching email or return not found
    :param login: the user username or email
    :return: json response containing user info or not found error
    """
    # check if login string is a username or email address
    if '@' in login:
        return redirect(url_for('api.users.get_user_by_email', email=login))
    else:
        return redirect(url_for('api.users.get_user_by_username', username=login))


@user.route('/add', methods=['POST'])
def add_user():
    """
    Create a new user based on the supplied data
    :return: json containing the user information of the newly created user
    """
    # if bcrypt.hashpw(password, user['password'].encode('utf-8')) == user['password'].encode('utf-8'):
    data = request.form
    username = data.get('username')
    firstname = data.get('firstname')
    lastname = data.get('lastname')
    email = data.get('email')
    password = data.get('password')
    pimg_url = data.get('pimg_url')

    # test if any required fields are empty or not supplied
    if not (username and firstname and lastname and email and password):
        return jsonify({"status": "error", "message": "missing required field(s)"})

    new_user = User(user_username=username,
                    user_firstname=firstname,
                    user_lastname=lastname,
                    user_email=email,
                    user_password=password,
                    user_contribution_score=0,
                    user_pimg_url=pimg_url)

    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('api.users.get_user_by_id',
                            user_id=new_user.user_id))


@user.route('/update', methods=['PUT'])
def update():
    # get the request form data with the updated attributes
    data = request.form
    user_id = data.get('user_id')

    # get the user object to update
    if user_id is not None:
        updated_user = User.query.get(user_id)
    else:
        return jsonify({"status": "error", "message": "user_id missing"})

    # check if the user exists, if not return None
    if updated_user is None:
        return jsonify({"status": "error", "message": "user not found"})
    # get the request form data with the updated attributes
    data = request.form
    username = data.get('username')
    firstname = data.get('firstname')
    lastname = data.get('lastname')
    email = data.get('email')
    password = data.get('password')
    contribution_score = data.get('contribution_score')
    # if no attribute given it defaults to None so don't update
    if lastname is not None:
        updated_user.user_lastname = lastname
    if firstname is not None:
        updated_user.user_firstname = firstname
    if email is not None:
        updated_user.user_email = email
    if username is not None:
        updated_user.user_username = username
    if password is not None:
        updated_user.user_password = password
    if contribution_score is not None:
        updated_user.user_contribution_score = contribution_score

    db.session.commit()

    return redirect(url_for('api.users.get_user_by_id',
                            user_id=updated_user.user_id))


@user.route('/delete', methods=['DELETE'])
def delete():
    user_id = request.form.get('user_id')
    if user_id is None:
        return jsonify({"status": "error", "message": "user_id missing"})
    user_delete = User.query.get(user_id)
    if user_delete:
        db.session.delete(user_delete)
        db.session.commit()
        return jsonify({"status": "success", "message": "user deleted"})
    else:
        return jsonify({"status": "error", "message": "user not found"})


@user.route('/deleteByEmail', methods=['DELETE'])
def delete_by_email():
    """
    Deletes a user corresponding to a given email
    :return: json response corresponding to success / fail
    """
    user_email = request.form.get('email')
    if user_email is None:
        return jsonify({"status": "error", "message": "email missing"})
    delete_user = User.query.filter_by(user_email=user_email).first()
    if delete_user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"status": "success", "message": "user deleted"})
    else:
        return jsonify({"status": "error", "message": "user not found"})


@user.route('/deleteAll', methods=['DELETE', 'GET'])
def delete_all():
    """
    Delete all users, mainly used for development
    """
    db.session.query(User).delete()
    db.session.commit()
    return redirect(url_for('api.users.get_users'))

