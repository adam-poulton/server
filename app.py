import json
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def main():
    return render_template('index.html')


@app.route("/barcode/<barcode_id>")
def barcode(barcode_id):
    return json.dumps({'barcode': barcode_id,
                       'name': 'peanut butter',
                       'brand': 'kraft'})


if __name__ == "__main__":
    app.run()
