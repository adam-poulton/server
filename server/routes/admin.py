from flask import Blueprint, jsonify, request, render_template
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from flask_uploads import UploadSet, IMAGES
from wtforms import SubmitField

from server.services import nutrition_detector as detect

admin = Blueprint('admin', __name__)

images = UploadSet('images', IMAGES)


class PhotoForm(FlaskForm):
    image = FileField(validators=[FileAllowed(images, 'Images only!'), FileRequired('Select an image')])
    submit = SubmitField('Scan Image')


@admin.route('/upload', methods=['GET', 'POST'])
def upload():
    form = PhotoForm()
    result = None

    if form.validate_on_submit():
        img = form.image.data
        result = detect.from_raw(img)

    return render_template('upload.html', form=form, result=result)


def process():
    if request.method == 'POST':
        image = request.files.get('image')
        url = request.form.get('url')
        if image:
            return jsonify(detect.from_raw(image))
        elif url:
            return jsonify(detect.from_url(url))
