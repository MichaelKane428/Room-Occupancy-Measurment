'''
    Michael Kane 2017

    Student No: C14402048
    course: DT211C
    Date: 12/11/2017

    Introduction:

    Step-by-Step:

    OverView:

    References:
    https://gist.github.com/yoavram/4351498
'''
import os
from flask import Flask, render_template, request, url_for


UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = ['jpg']
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowedFile(filename):
    return filename[-3:].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=['GET','POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowedFile(file.filename):
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return url_for('uploaded_file', filename=filename)
    return '''
    <p>latest image</p>
    <img src=>
    '''


if __name__ == "__main__":
    app.run(host="192.168.0.9", port=5000)
