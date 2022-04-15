from sqlalchemy import Integer, Column, String, DateTime, DECIMAL, Float
from sqlalchemy.sql import func
from sqlalchemy.schema import ForeignKey
from dataclasses import dataclass

from server.database import Base


@dataclass
class User(Base):
    __tablename__ = 'User'
    user_id: int
    user_username: str
    user_firstname: str
    user_lastname: str
    user_email: str
    user_password: str
    user_contribution_score: int
    user_pimg_url: str
    user_hash: str

    user_id = Column(Integer, autoincrement=True, primary_key=True)
    user_username = Column(String(30), nullable=False, unique=True)
    user_firstname = Column(String(30), nullable=False)
    user_lastname = Column(String(30), nullable=False)
    user_email = Column(String(40), nullable=False, unique=True)
    user_password = Column(String(50))
    user_contribution_score = Column(Integer(), default=0)
    user_pimg_url = Column(String(256))
    user_hash = Column(String(150), nullable=True)


@dataclass
class Product(Base):
    __tablename__ = 'Product'
    product_id: int
    product_barcode: str
    product_name: str
    product_cate: str
    product_brand: str
    product_nutrition: str
    product_price: float

    product_id = Column(Integer, primary_key=True)
    product_barcode = Column(String(20), unique=True, nullable=False)
    product_name = Column(String(100), nullable=False)
    product_cate = Column(String(50))
    product_brand = Column(String(50), nullable=False)
    product_nutrition = Column(String(900))
    product_price = Column(Float)


@dataclass
class Favourite(Base):
    __tablename__ = 'Favourite'
    favourite_id: int
    product_id: int
    user_id: int

    favourite_id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("Product.product_id"), nullable=False)
    user_id = Column(Integer, ForeignKey("User.user_id"), nullable=False)


@dataclass
class Scan(Base):
    __tablename__ = 'Scan'
    scan_id: int
    product_id: int
    user_id: int
    timestamp: str

    scan_id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("Product.product_id"), nullable=False)
    user_id = Column(Integer, ForeignKey("User.user_id"), nullable=False)
    timestamp = Column(DateTime(timezone=True), default=func.now())


@dataclass
class Feedback(Base):
    feedback_id: int
    user_id: int
    feedback_description: str
    feedback_date: str
    feedback_rating: float

    __tablename__ = 'Feedback'
    feedback_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("User.user_id"), nullable=False)
    feedback_description = Column(String(300),  nullable=False)
    feedback_date = Column(DateTime(timezone=True), default=func.now(), nullable=False)
    feedback_rating = Column(DECIMAL(2, 1), nullable=False)