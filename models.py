from sqlalchemy.sql import func
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

# class Scan_record(db.Model):
#     scan_date = db.Column(db.DateTime(timezone=True), default=func.now())
#     user_id = db.Column(db.Integer, db.ForeignKey('User.user_id'), primary_key=True)
#

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    user_fName = db.Column(db.String(20))
    user_lName = db.Column(db.String(20))
    user_email = db.Column(db.String(35))
    user_password = db.Column(db.String(50))
    # scan_record = db.relationship('Scan_record')

class Product(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    product_barcode = db.Column(db.String(45))
    product_name = db.Column(db.String(45))
    product_cate = db.Column(db.String(45))
    product_brand = db.Column(db.String(45))