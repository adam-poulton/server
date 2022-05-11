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

    if request.method == 'POST':
        img = form.image.data.read()
        url = cloud_upload.upload(img)['secure_url']
        result = detect.from_url(url)
        return render_template('upload.html', form=form, result=result, url=url)

    return render_template('upload.html', form=form)
