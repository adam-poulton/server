from sqlalchemy.sql import func
from sqlalchemy.schema import ForeignKey
from sqlalchemy.types import JSON
from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass

db = SQLAlchemy()


@dataclass
class User(db.Model):
    user_id: int
    user_username: str
    user_firstname: str
    user_lastname:str
    user_email:str
    user_password:str
    user_contribution_score: int
    user_pimg_url:str

    user_id = db.Column(db.Integer(11), autoincrement=True, primary_key=True)
    user_username = db.Column(db.String(30), nullable=False, unique=True)
    user_firstname = db.Column(db.String(30), nullable=False)
    user_lastname = db.Column(db.String(30), nullable=False)
    user_email = db.Column(db.String(40), nullable=False, unique=True)
    user_password = db.Column(db.String(50))
    user_contribution_score = db.Column(db.Integer(11), default=0)
    user_pimg_url = db.Column(db.String(256))


@dataclass
class Product(db.Model):
    product_id: int
    product_barcode: str
    product_name: str
    product_cate: str
    product_brand: str
    product_nutrition: str

    product_id = db.Column(db.Integer, primary_key=True)
    product_barcode = db.Column(db.String(45), unique=True, nullable=False)
    product_name = db.Column(db.String(45), nullable=False)
    product_cate = db.Column(db.String(45))
    product_brand = db.Column(db.String(45), nullable=False)
    product_nutrition = db.Column(JSON)


@dataclass
class Favourite(db.Model):
    favourite_id: int
    product_id: int
    user_id: int

    favourite_id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, ForeignKey("Product.product_id"), nullable=False)
    user_id = db.Column(db.Integer, ForeignKey("User.user_id"), nullable=False)


@dataclass
class Scan(db.Model):
    scan_id: int
    product_id: int
    user_id: int

    scan_id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, ForeignKey("Product.product_id"), nullable=False)
    user_id = db.Column(db.Integer, ForeignKey("User.user_id"), nullable=False)
    timestamp = db.Column(db.DateTime(timezone=True), default=func.now())
