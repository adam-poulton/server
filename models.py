from sqlalchemy.sql import func
from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass

db = SQLAlchemy()

# class Scan_record(db.Model):
#     scan_date = db.Column(db.DateTime(timezone=True), default=func.now())
#     user_id = db.Column(db.Integer, db.ForeignKey('User.user_id'), primary_key=True)
#

@dataclass
class User(db.Model):
    user_id: int
    user_fName: str
    user_lName:str
    user_email:str

    user_id = db.Column(db.Integer, primary_key=True)
    user_fName = db.Column(db.String(20))
    user_lName = db.Column(db.String(20))
    user_email = db.Column(db.String(35))
    user_password = db.Column(db.String(50))
    # scan_record = db.relationship('Scan_record')


@dataclass
class Product(db.Model):
    product_id:int
    product_barcode:str
    product_name:str
    product_cate:str
    product_brand:str

    product_id = db.Column(db.Integer, primary_key=True)
    product_barcode = db.Column(db.String(45))
    product_name = db.Column(db.String(45))
    product_cate = db.Column(db.String(45))
    product_brand = db.Column(db.String(45))