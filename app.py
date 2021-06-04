import os
from flask import Flask, request, redirect, url_for, send_from_directory, render_template

from werkzeug.utils import secure_filename
import numpy as np


ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'png'])
IMAGE_SIZE = (150, 150)
UPLOAD_FOLDER = 'uploads'

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = os.path.join('static/bonn/')
image_list = glob.glob(IMAGE_PATH+'*.png')



app = Flask(__name__, template_folder='Templates')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS




@app.route("/")
def template_test():
    return render_template('home.html', label='', imagesource='file://null')


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        id_image = int(request.form['id_image'])
        file_path = os.path.join(image_list[id_image])
        output = {'Negative:': 0, 'Positive': 1}
    return render_template("home.html", label=output, imagesource=file_path)


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

if __name__ == "__main__":
    app.run(threaded=True,debug=True)
