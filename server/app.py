from server import create_app
from .models import db, Product, User

app = create_app()
app.app_context().push()


def insert_data():
    products = [
        {
            "name": "Savoy Original",
            "brand": "Arnott's",
            "barcode": "9310072026428",
            "category": "Biscuits",
            "nutrition":
                {
                    "energy": [1970.0, "kJ"],
                    "protein": [7.9, "g"],
                    "fat-total": [20.0, "g"],
                    "fat-saturated": [3.9, "g"],
                    "carbohydrate": [62.6, "g"],
                    "sugars": [1.3, "g"],
                    "sodium": [848, "mg"]
                }
        },
        {
            "name": "Lindor Extra Dark 18pc",
            "brand": "Lindt",
            "barcode": "7610400074193",
            "category": "Chocolate",
            "nutrition":
                {
                    "energy": [2670.0, "kJ"],
                    "protein": [4.9, "g"],
                    "fat-total": [53.0, "g"],
                    "fat-saturated": [39.0, "g"],
                    "carbohydrate": [34.0, "g"],
                    "sugars": [31.0, "g"],
                    "sodium": [16, "mg"]
                }
        },
        {
            "name": "Mi Goreng Fried Noodles Cup",
            "brand": "Indo mie",
            "barcode": "08968618065",
            "category": "Noodles",
            "nutrition":
                {
                    "energy": [942.0, "kJ"],
                    "protein": [3.4, "g"],
                    "fat-total": [10.4, "g"],
                    "fat-saturated": [4.9, "g"],
                    "carbohydrate": [29.3, "g"],
                    "sugars": [3.8, "g"],
                    "sodium": [450, "mg"]
                }
        },
        {
            "name": "Sweet Potato & Roasted Cashews Dip",
            "brand": "Yumi's",
            "barcode": "93174440001168",
            "category": "Dips",
            "nutrition":
                {
                    "energy": [1050, "kJ"],
                    "protein": [3.7, "g"],
                    "fat-total": [21.0, "g"],
                    "fat-saturated": [2.4, "g"],
                    "carbohydrate": [11.0, "g"],
                    "sugars": [5.1, "g"],
                    "sodium": [394, "mg"]
                }
        },
        {
            "name": "Sea Salt & Balsamic Vinegar Flavoured Potato Chips",
            "brand": "Red Rock Deli",
            "barcode": "9310015240638",
            "category": "Potato Chips",
            "nutrition":
                {
                    "energy": [2050, "kJ"],
                    "protein": [7.6, "g"],
                    "fat-total": [23.8, "g"],
                    "fat-saturated": [1.9, "g"],
                    "fat-trans": [0.1, "g"],
                    "fat-poly": [2.3, "g"],
                    "fat-mono": [5.4, "g"],
                    "carbohydrate": [11.0, "g"],
                    "sugars": [5.1, "g"],
                    "sodium": [394, "mg"]
                }
        },
        {
            "name": "Spelt & Sprouted Grain Bread",
            "brand": "Alpine Breads",
            "barcode": "9312743010521",
            "category": "Spelt Bread",
            "nutrition":
                {
                    "energy": [988, "kJ"],
                    "protein": [11.9, "g"],
                    "fat-total": [1.6, "g"],
                    "fat-saturated": [0.6, "g"],
                    "fat-trans": [0.1, "g"],
                    "fat-poly": [2.3, "g"],
                    "fat-mono": [5.4, "g"],
                    "carbohydrate": [39.7, "g"],
                    "sugars": [5.1, "g"],
                    "sodium": [394, "mg"]
                }
        }
    ]
    for product in products:
        db.session.add(
            Product(product_barcode=product['barcode'],
                    product_name=product['name'],
                    product_brand=product['brand'],
                    product_cate=product['category'],
                    product_nutrition=product['nutrition']
                    )
        )
    users = [
        {
            "user_contribution_score": 0,
            "user_email": "asd@gmail.com",
            "user_firstname": "asd",
            "user_id": 9084,
            "user_lastname": "asd",
            "user_password": "n7DxlL8d",
            "user_pimg_url": None,
            "user_username": "asd"
        },
        {
            "user_contribution_score": 0,
            "user_email": "zxc@gmail.com",
            "user_firstname": "zxc",
            "user_id": 9974,
            "user_lastname": "zxc",
            "user_password": "asdasdasdA",
            "user_pimg_url": None,
            "user_username": "zxc"
        },
        {
            "user_contribution_score": 0,
            "user_email": "xcv@gmail.com",
            "user_firstname": "xcv",
            "user_id": 9984,
            "user_lastname": "xcv",
            "user_password": "xcvxcvxcvX",
            "user_pimg_url": None,
            "user_username": "xcv"
        },
        {
            "user_contribution_score": 0,
            "user_email": "zxcc@gmail.com",
            "user_firstname": "zxc",
            "user_id": 10004,
            "user_lastname": "zxc",
            "user_password": "zxczxczxcZ",
            "user_pimg_url": None,
            "user_username": "zxcc"
        },
        {
            "user_contribution_score": 0,
            "user_email": "1395141398@qq.com",
            "user_firstname": "Caius",
            "user_id": 10034,
            "user_lastname": "Zhou",
            "user_password": "abcdefgAH",
            "user_pimg_url": "https://graph.facebook.com/3001150743533610/picture?type=normal",
            "user_username": "3001150743533610"
        },
        {
            "user_contribution_score": 0,
            "user_email": "bnm@gmail.com",
            "user_firstname": "bnm",
            "user_id": 10044,
            "user_lastname": "bnm",
            "user_password": "bnmbnmbnmA",
            "user_pimg_url": None,
            "user_username": "bnm"
        },
        {
            "user_contribution_score": 0,
            "user_email": "jkl@gmail.com",
            "user_firstname": "kl",
            "user_id": 10054,
            "user_lastname": "jkl",
            "user_password": "TD2UTWX2",
            "user_pimg_url": None,
            "user_username": "jklj"
        },
        {
            "user_contribution_score": 0,
            "user_email": "tyu@gmail.com",
            "user_firstname": "tyu",
            "user_id": 10064,
            "user_lastname": "tyu",
            "user_password": "WQxV5kJk",
            "user_pimg_url": None,
            "user_username": "tyu"
        },
        {
            "user_contribution_score": 0,
            "user_email": "adamp@123.com",
            "user_firstname": "adam",
            "user_id": 10084,
            "user_lastname": "poulton",
            "user_password": "",
            "user_pimg_url": None,
            "user_username": "adamp234"
        },
        {
            "user_contribution_score": 1000,
            "user_email": "adam3p1@123.com",
            "user_firstname": "John",
            "user_id": 10094,
            "user_lastname": "poulton",
            "user_password": "1234test",
            "user_pimg_url": None,
            "user_username": "adamp23455"
        },
        {
            "user_contribution_score": 0,
            "user_email": "adap1@123.com",
            "user_firstname": "adam",
            "user_id": 10114,
            "user_lastname": "poulton",
            "user_password": None,
            "user_pimg_url": None,
            "user_username": "adamp2"
        },
        {
            "user_contribution_score": 0,
            "user_email": "yinghua.zho@gmail.com",
            "user_firstname": "Yinghua",
            "user_id": 10124,
            "user_lastname": "Zhou",
            "user_password": None,
            "user_pimg_url": "https://lh3.googleusercontent.com/a-/AOh14Gj37N6HOGaEbt0suhVQo1tRkqoaFpg2YSkB-DWE=s96-c",
            "user_username": "10491897129537300745"
        },
        {
            "user_contribution_score": 0,
            "user_email": "abcdefg@gmail.com",
            "user_firstname": "Abc",
            "user_id": 10134,
            "user_lastname": "Defg",
            "user_password": "abcdefgA",
            "user_pimg_url": None,
            "user_username": "abcdefg"
        }
    ]
    for user in users:
        db.session.add(
            User(user_email=user['user_email'],
                 user_firstname=user['user_firstname'],
                 user_lastname=user['user_lastname'],
                 user_contribution_score=user['user_contribution_score'],
                 user_password=user['user_password'],
                 user_pimg_url=user['user_pimg_url'],
                 user_username=user['user_username']
                 )
        )
    db.session.commit()


# Drop and repopulate the database
with app.app_context():
    # db.drop_all()
    db.create_all()
    insert_data()


if __name__ == "__main__":
    app.run(debug=True)
    # print("In module products __package__, __name__ ==", __package__, __name__)
