from flask import Blueprint, render_template, url_for, request, jsonify, json
from werkzeug.utils import redirect

from ..models import User, db

user = Blueprint('users', __name__)


@user.route('/display', methods=['GET'])
def get_users_display():
    return render_template('users.html', Users=User.query.all())


@user.route('/get', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify(users)


@user.route('/get/<user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user_match = User.query.get(user_id)
    return jsonify(user_match)


@user.route('/getbyEmail/<email>', methods=['GET'])
def get_user_by_email(email):
    # params = [i for i in request.args.keys()]
    user_match = User.query.filter_by(user_email=email).first()
    return jsonify(user_match.first())


@user.route('/add', methods=['POST'])
def add_user():
    # if bcrypt.hashpw(password, user['password'].encode('utf-8')) == user['password'].encode('utf-8'):
    data = request.form
    username = data['username']
    firstname = data['firstname']
    lastname = data['lastname']
    email = data['email']
    password = data['password']

    new_user = User(user_username=username,
                    user_firstname=firstname,
                    user_lastname=lastname,
                    user_email=email,
                    user_password=password,
                    user_contributionscore=0)

    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('api.users.get_user_by_id', user_id=new_user.user_id))


@user.route('/update', methods=['PUT'])
def update():
    # get the request form data with the updated attributes
    data = request.form
    user_id = data.get('user_id')
    username = data.get('username')
    firstname = data.get('firstname')
    lastname = data.get('lastname')
    email = data.get('email')
    password = data.get('password')
    contributionscore = data.get('contributionscore')

    # get the user object to update
    if user_id is not None:
        updated_user = User.query.get(user_id)
    else:
        return jsonify({"error": "user_id not supplied"})

    # check if the user exists, if not return None
    if updated_user is None:
        return jsonify({"error": "user not found"})
    # get the request form data with the updated attributes
    data = request.form
    username = data.get('username')
    firstname = data.get('firstname')
    lastname = data.get('lastname')
    email = data.get('email')
    password = data.get('password')
    contributionscore = data.get('contributionscore')
    # if no attribute given it defaults to None so don't update
    if lastname is not None:
        updated_user.user_lastname = lastname
    if firstname is not None:
        updated_user.user_firstname = firstname
    if email is not None:
        updated_user.user_email = email
    if password is not None:
        updated_user.user_password = password
    if contributionscore is not None:
        updated_user.user_contributionscore = contributionscore

    db.session.commit()

    return redirect(url_for('api.users.get_user_by_id', user_id=updated_user.user_id))


@user.route('/delete', methods=['DELETE'])
def delete():
    user_id = request.args.get('user_id')
    user_delete = User.query.get(user_id)
    if user_delete:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"success": "user deleted"})
    else:
        return jsonify({"error": "user not found"})


@user.route('/deleteAll', methods=['DELETE', 'GET'])
def delete_all():
    db.session.query(User).delete()
    db.session.commit()
    return redirect(url_for('api.users.get_users'))
