import json
from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# connect to mysql server
connection = mysql.connector.connect(
    host='localhost',
    user='ydin0039',
    password='StevenDing0039',
    port='3306',
    database='fit3162'
)
cur = connection.cursor()   # main operation done by mysql cursor

def addUsers():
    fname, lname, email, password = "1", "1", "1", "1"

    addUser_command = """INSERT INTO users (user_firstName,
                                            user_lastName,
                                            user_email, 
                                            user_password)
    VALUES (%s,%s,%s,%s)"""

    cur.execute(addUser_command, (fname, lname, email, password))
    connection.commit()

def getUsers():
    cur = connection.cursor()
    cur.execute("select * from users")
    users = cur.fetchall()
    for user in users:
        print("user id: ",user[0])
        print("user first name", user[1])
        print("user last name", user[2])
        print("user email", user[3])
        print("  ")


addUsers()  # the operation to add user
getUsers()    # get all users

connection.close()
cur.close()
print("MySQL connection is closed")


@app.route("/")
def main():
    return render_template('index.html')

@app.route("/barcode/<barcode_id>")
def barcode(barcode_id):
    return json.dumps({'barcode': barcode_id,
                       'name': 'peanut butter',
                       'brand': 'kraft'})


if __name__ == "__main__":
    app.run(debug=True)
