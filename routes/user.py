from flask import Blueprint, render_template, url_for
from werkzeug.utils import redirect

from ..models import User, db

user = Blueprint('users', __name__)

@user.route('/')
def getUsers():
    return render_template('users.html', Users=User.query.all())

@user.route('/addUser')
def addUser():
    user = User(user_fName ="steven",user_lName = "ding",user_email=  "aaa@gmail.com",user_password= "123456")
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('users.getUsers'))