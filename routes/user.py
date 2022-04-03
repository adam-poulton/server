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

@user.route('/getbyEmail/<email>', methods=['GET'])
def getUserByEmail(email):
    # params = [i for i in request.args.keys()]
    user = User.query.filter_by(user_email=email)
    return jsonify(user.first())

@user.route('/add', methods=['POST'])
def addUser():
    # if bcrypt.hashpw(password, user['password'].encode('utf-8')) == user['password'].encode('utf-8'):
    data = request.form
    userName = data['userName']
    lname = data['lname']
    fname = data['fname']
    email = data['email']
    password = data['password']


    user = User(user_userName=userName, user_fName=fname, user_lName=lname, user_email=email, user_password=password, user_contributionScore=0)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('api.users.getUsers'))


@user.route('/update/<id>', methods=['PUT', 'GET'])
def update(id):
    user = User.query.get(id)

    lName = request.args.get('lname', None)
    fName = request.args.get('fname', None)
    email = request.args.get('email', None)
    password = request.args.get('password', None)

    if lName != None:
        user.user_lName = lName
    if fName != None:
        user.user_fName = fName
    if email != None:
        user.user_email = email
    if password != None:
        user.user_password = password

    db.session.commit()

    return jsonify(user)


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
