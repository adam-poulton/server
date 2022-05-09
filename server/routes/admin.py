from flask import Blueprint, jsonify, request, render_template
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired

from server.services import nutrition_detector as detect

admin = Blueprint('admin', __name__)


class PhotoForm(FlaskForm):
    image = FileField(validators=[FileRequired()])


@admin.route('/upload', methods=['GET', 'POST'])
def upload():
    form = PhotoForm()

    if form.validate_on_submit():
        img = form.image.data
        return jsonify(detect.from_raw(img))

    return render_template('upload.html', form=form)


def process():
    if request.method == 'POST':
        image = request.files.get('image')
        url = request.form.get('url')
        if image:
            return jsonify(detect.from_raw(image))
        elif url:
            return jsonify(detect.from_url(url))
