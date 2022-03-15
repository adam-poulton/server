import json
from flask import Flask, render_template
from db import db

app = Flask(__name__)

def addUsers():
    cur = db.cursor()  # operation done by mysql cursor
    fname, lname, email, password = "1", "1", "1", "1"

    addUser_command = """INSERT INTO users (user_firstName,
                                            user_lastName,
                                            user_email, 
                                            user_password)
    VALUES (%s,%s,%s,%s)"""

    cur.execute(addUser_command, (fname, lname, email, password))
    db.commit()
    cur.close()


@app.route("/")
def main():
    return render_template('index.html')


@app.route("/getusers")
def getUsers():
    cur = db.cursor()  # operation done by mysql cursor
    cur.execute("select * from users")
    users = cur.fetchall()  # list of list of user info
    if len(users) > 0:
        return render_template('users.html', userDetails=users)
    cur.close()
    return """<h1>Not user data found</h1>"""


def deleteAllUsers():
    def deleteAllUsers():
        cur = db.cursor()  # operation done by mysql cursor
        cur.execute("delete from users")
        db.commit()
        cur.close()
        return "all users are deleted"


@app.route("/barcode/<barcode_id>")
def barcode(barcode_id):
    return json.dumps({'barcode': barcode_id,
                       'name': 'peanut butter',
                       'brand': 'kraft'})

addUsers()  # the operation to add user


if __name__ == "__main__":
    app.run(debug=True)

