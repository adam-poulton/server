import cloudinary.uploader as cloud_upload
from flask import Blueprint, jsonify, request, render_template
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import SubmitField
import sys

from server.services import nutrition_detector as detect

admin = Blueprint('admin', __name__)


class PhotoForm(FlaskForm):
    image = FileField(validators=[FileRequired('Select an image')])
    submit = SubmitField('Scan Image')


@admin.route('/upload', methods=['GET', 'POST'])
def upload():
    form = PhotoForm()
    result = {'sodium': {'value': 848.0, 'unit': 'mg'}, 'carbohydrate': {'value': 62.6, 'unit': 'g'},
              'protein': {'value': 7.9, 'unit': 'g'}, 'energy': {'value': 1970.0, 'unit': 'kJ'},
              'fat-total': {'value': 20.0, 'unit': 'g'}, 'sugars': {'value': 1.3, 'unit': 'g'},
              'fat-saturated': {'value': 3.9, 'unit': 'g'}}

    if form.validate_on_submit():
        img = form.image.data
        url = cloud_upload.upload(img)['secure_url']
        print(f'{url}', file=sys.stderr)
        result = detect.from_url(url)
        print(f'{result}', file=sys.stderr)

    return render_template('upload.html', form=form, result=result)


def process():
    if request.method == 'POST':
        image = request.files.get('image')
        url = request.form.get('url')
        if image:
            return jsonify(detect.from_raw(image))
        elif url:
            return jsonify(detect.from_url(url))
