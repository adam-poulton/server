from server import create_app, seed_app

app = create_app()
app.app_context().push()


if __name__ == "__main__":
    app.run(debug=True)
    seed_app()
    # print("In module products __package__, __name__ ==", __package__, __name__)
