import os

from flask import Blueprint, render_template, url_for, request, jsonify, json, Response
from werkzeug.utils import redirect
import bcrypt
import cloudinary.uploader as cloud_upload
from server.database import db_session
from server.models import User

user = Blueprint('user', __name__)


basedir = os.getcwd()
image_path = os.path.join(basedir, 'server', 'data', 'images')


@user.route('/display', methods=['GET'])
def get_users_display():
    """
    Returns all users in the database in html table form, mainly used for development
    """
    return render_template('users.html', Users=User.query.all())


@user.route('/login', methods=['POST'])
def login():
    """
    Validates a user login by a given username and password
    Returns the logged in user object or an error
    """
    username = request.form.get('username')
    password = request.form.get('password')

    if not username:
        return 'missing username', 405
    if not password:
        return 'missing password', 406

    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


@user.route('/register', methods=['POST'])
def register():
    """
    Registers a user by a given username and password
    Returns the logged in user object or an error
    """
    data = request.form
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    firstname = data.get('firstname')
    lastname = data.get('lastname')
    pimg_url = data.get('pimg_url')

    if not username:
        return 'missing username', 405
    if not password:
        return 'missing password', 406

    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    with db_session() as session:
        new_user = User(user_username=username,
                        user_email=email,
                        user_firstname=firstname,
                        user_hash=hashed,
                        user_lastname=lastname,
                        user_pimg_url=pimg_url,
                        user_contribution_score=0
                        )
        session.add(new_user)
        session.commit()
        return jsonify(new_user.to_dict())


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


@user.route('/get/<user_id>/favourite', methods=['GET'])
def get_user_favourites(user_id):
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


@user.route('/getBy/<login>', methods=['GET'])
def get_user_by(login):
    """
    Return a matched user in json form with matching email or return not found
    :param login: the user username or email
    :return: json response containing user info or not found error
    """
    # check if login string is a username or email address
    if '@' in login:
        return redirect(url_for('api.user.get_user_by_email', email=login))
    else:
        return redirect(url_for('api.user.get_user_by_username', username=login))


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
    if not (username and firstname and lastname and email):
        return jsonify({"status": "error", "message": "missing required field(s)"})

    with db_session() as session:
        # test if username and email are unique
        new_username = session.query(User).filter_by(user_username=username).first()
        new_email = session.query(User).filter_by(user_email=email).first()
        if new_username is not None:
            return Response(
                json.dumps({"status": "error", "message": "username already exists"}),
                status=405,
                mimetype='application/json')
        if new_email is not None:
            return Response(
                json.dumps({"status": "error", "message": "email already exists"}),
                status=406,
                mimetype='application/json')

        new_user = User(user_username=username,
                        user_firstname=firstname,
                        user_lastname=lastname,
                        user_email=email,
                        user_password=password,
                        user_contribution_score=0,
                        user_pimg_url=pimg_url)
        session.add(new_user)
        session.commit()
        return jsonify(new_user)


@user.route('/update', methods=['PUT'])
def update():
    # get the request form data with the updated attributes
    data = request.form
    user_id = data.get('user_id')
    if user_id is None:
        return jsonify({"status": "error", "message": "user_id missing"})
    with db_session() as session:
        # get the user object to update
        updated_user = session.query(User).get(user_id)
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
        # commit changes
        session.commit()
        return jsonify(updated_user)


@user.route('/delete', methods=['DELETE'])
@user.route('/delete/<user_id>', methods=['DELETE'])
def delete(user_id=None):
    """
    Deletes a user corresponding to a given id
    :return: json response corresponding to success / fail
    """
    if user_id is None:
        return jsonify({"status": "error", "message": "user_id missing"})
    with db_session() as session:
        user_delete = session.query(User).get(user_id)
        if user_delete is None:
            return jsonify({"status": "error", "message": "user not found"})
        session.delete(user_delete)
        session.commit()
        return jsonify({"status": "success", "message": "user deleted"})


@user.route('/deleteByEmail', methods=['DELETE'])
def delete_by_email():
    """
    Deletes a user corresponding to a given email
    :return: json response corresponding to success / fail
    """
    user_email = request.form.get('email')
    if user_email is None:
        return jsonify({"status": "error", "message": "email missing"})
    with db_session() as session:
        user_delete = session.query(User).filter_by(user_email=user_email).first()
        if user_delete is None:
            return jsonify({"status": "error", "message": "user not found"})
        session.delete(user_delete)
        session.commit()
        return jsonify({"status": "success", "message": "user deleted"})


@user.route('/deleteAll', methods=['DELETE', 'GET'])
def delete_all():
    """
    Delete all users, mainly used for development
    """
    with db_session() as session:
        session.query(User).delete()
        session.commit()
    return redirect(url_for('api.user.get_users'))


@user.route('/profileImg', methods=['PUT'])
def profile_img():
    """
    Upload user's profile image
    """
    data = request.form
    user_id = data.get('user_id')

    # parse the request images
    pimg = request.files.get('profile_img')
    if pimg:
        response = cloud_upload.upload(pimg)
        profile_img_url = response['secure_url']

        with db_session() as session:
            # get the user object to update
            updated_user = session.query(User).get(user_id)
            if updated_user:
                updated_user.user_pimg_url = profile_img_url
                session.commit()
                return jsonify({"user_pimg_url": updated_user.user_pimg_url})
            else:
                return jsonify({"status": "error", "message": "user not found"})
    else:
        return jsonify({"status": "error", "message": "image not found"})
