from server import create_app
from .models import db, Product, User

app = create_app()



if __name__ == "__main__":
    app.run(debug=True)
    # print("In module products __package__, __name__ ==", __package__, __name__)
