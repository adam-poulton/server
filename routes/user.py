from flask import Blueprint, render_template, url_for, request, jsonify, json
from werkzeug.utils import redirect

from ..models import User, db

user = Blueprint('users', __name__)


@user.route('/display', methods= ['GET'])
def getUsers_inTable():
    return render_template('users.html', Users=User.query.all())


@user.route('/get', methods=['GET'])
def getUsers():
    users = User.query.all()
    return jsonify(users)


@user.route('/getByEmail/<email>', methods=['GET'])
def getUserByEmail(email):
    # params = [i for i in request.args.keys()]
    user = User.query.filter_by(user_email=email).first()
    if user:
        return jsonify(user)
    else:
        return jsonify({"message": "user not found"})


@user.route('/add', methods=['POST'])
def addUser():
    # if bcrypt.hashpw(password, user['password'].encode('utf-8')) == user['password'].encode('utf-8'):
    data = request.form
    username = data['username']
    lname = data['lastname']
    fname = data['firstname']
    email = data['email']
    password = data['password']

    user = User(user_username=username, user_firstname=fname, user_lastname=lname, user_email=email, user_password=password, user_contributionscore=0)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('api.users.getUsers'))


@user.route('/updatepassword/<email>', methods=['PUT'])
def update(email):
    user = User.query.filter_by(user_email=email).first()
    if user:
        data = request.form
        password = data['password']
        user.user_password = password
        db.session.commit()
        return jsonify(user)
    else:
        return jsonify({"message": "user not found"})


@user.route('/delete/<id>', methods=['DELETE', 'GET'])
def delete(id):

    user = User.query.get(id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return redirect(url_for('api.users.getUsers'))
    else:
        return jsonify({"message": "user not found"})


@user.route('/deleteAll', methods=['DELETE', 'GET'])
def deleteAll():
    db.session.query(User).delete()
    db.session.commit()
    return redirect(url_for('api.users.getUsers'))

