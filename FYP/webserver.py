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
from flask_cors import CORS


UPLOAD_FOLDER = 'D:\\Python\\Room-Occupancy-Measurment\\FYP\\Uploads\\'
ALLOWED_EXTENSIONS = ['jpg']
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORS(app)

def login():
    pass
	
def gallery():
    pass

def encryptPassword():
    pass
	
def Register():
    pass
	
def saveImage():
    pass
	
def pullImage():
    pass
	
def getStatistics():
    pass

def allowedFile(filename):
    return filename[-3:].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print("We made it to step one")
        file = request.files['file']
        print("We made it to step one.5")
        if file and allowedFile(file.filename):
            print("We made it to step two")
            filename = file.filename
            print(filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print("We made it boys")
            return '''<p> it worked</p>'''
    return '''
  <!doctype html>
  <title>Upload new File</title>
  <h1>UPload new File</h1>
  <form action="" method=post enctype=multipart/form-data>
  <p><input type=file name=file>
  <input type=submit value=Upload>
  </form>
  '''
if __name__ == "__main__":
    app.run(host="192.168.0.9", port=5000)
