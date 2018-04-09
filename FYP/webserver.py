'''
    Michael Kane 2017

    Student No: C14402048
    course: DT211C
    Date: 12/11/2017

    Introduction:

    Step-by-Step:

    OverView: This is

    References:
    https://gist.github.com/yoavram/4351498
    https://www.youtube.com/watch?v=T1ZVyY1LWOg
    https://pymotw.com/2/gc/
    https://www.youtube.com/watch?v=PiphizBQJho&index=16&list=PLQVvvaa0QuDc_owjTbIY4rbgXOFkUYOUB
    https://www.youtube.com/playlist?list=PLQVvvaa0QuDc_owjTbIY4rbgXOFkUYOUB
    https://stackoverflow.com/questions/27539309/how-do-i-create-a-link-to-another-html-page
    https://dev.mysql.com/doc/refman/5.7/en/json-creation-functions.html#function_json-object
    https://www.makeuseof.com/tag/python-javascript-communicate-json/
    http://jquery.malsup.com/cycle2/demo/
    http://jquery.malsup.com/cycle2/demo/basic.php
    https://stackoverflow.com/questions/4714975/how-to-select-the-last-10-rows-of-an-sql-table-which-has-no-id-field/14057040
    http://developer.rhino3d.com/guides/rhinopython/python-xml-json/
    https://stackoverflow.com/questions/11875770/how-to-overcome-datetime-datetime-not-json-serializable

'''
import os
from flask import Flask, render_template, request, url_for, flash, session, redirect
import gc
from flask_cors import CORS
from FYP import databaseconnection as db
import json
import base64

UPLOAD_FOLDER = 'D:\\Python\\Room-Occupancy-Measurment\\FYP\\static\\Uploads\\'
ALLOWED_EXTENSIONS = ['jpg']
app = Flask(__name__)
app.secret_key = 'Mikey1ne'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORS(app)


def allowedFile(filename):
    return filename[-3:].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=['GET'])
def home():
    return render_template("home.html")


@app.route("/upload/", methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        number_of_people = request.form['number_of_people']

        print(file)
        print(number_of_people)

        if file and allowedFile(file.filename):
            dbcursor, conn = db.login_connection()

            filename = file.filename
            date_time = filename[0:19]
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            path = 'D:/Python/Room-Occupancy-Measurment/FYP/static/uploads/' + filename
            query = ("insert into store_image (path, date_time, number_of_people) values ('%s', '%s', %s)", path, date_time, number_of_people)

            print(query)

            return redirect(url_for("gallery"))
    return render_template("uploadImage.html")


@app.route("/login/", methods=['GET', 'POST'])
def login():
    error = ''
    try:
        if request.method == 'POST':
            dbcursor, conn = db.login_connection()

            username = request.form['username']
            password = request.form['password']

            query = dbcursor.execute("select * from login_details where username = (%s) AND password = (%s)",
                                     (username, password))
            if query > 0:
                session['Logged_in'] = True
                session['user'] = username
                dbcursor.close()
                conn.close()
                gc.collect()
                return redirect(url_for("home"))
            else:
                print("Login Failed try again.")
                dbcursor.close()
                conn.close()
                gc.collect()
                return redirect(url_for("login"))

        return render_template("login.html", error=error)

    except Exception as e:
        return str(e)


@app.route("/register/", methods=['GET', 'POST'])
def register():
    error = ''
    try:
        if request.method == 'POST':
            dbcursor, conn = db.login_connection()

            username = request.form['username']
            password = request.form['password']
            confirmpassword = request.form['confirmpassword']
            email = request.form['email']
            if password == confirmpassword:
                query = dbcursor.execute("select * from login_details where username = (%s)", (username,))
                if query > 0:

                    dbcursor.close()
                    conn.close()
                    gc.collect()
                    return render_template("register.html")

                else:
                    query = dbcursor.execute(
                        "insert into login_details (username, password, email) values ((%s), (%s), (%s))",
                        (username, password, email))
                    conn.commit()
                    dbcursor.close()
                    conn.close()
                    gc.collect()
                    session['Logged_in'] = True
                    session['user'] = username
                return redirect(url_for("home"))
            else:
                print("passwords do not match please try again")
                return redirect(url_for("register"))
        return render_template("register.html", error=error)

    except Exception as e:
        return str(e)


@app.route("/gallery/", methods=['GET', 'POST'])
def gallery():
    error = ''
    datetime = ""
    try:
        if request.method == 'POST':
            temp = request.form['datepicker']
            datetime = temp.replace("T", " ")
            query1, query2, latestImages, datetimeImages = createquery(datetime)

            if query1 > 0 and query2 > 0:
                return render_template("gallery.html", latestimages=json.dumps(latestImages, default=str), datetimeimages=json.dumps(datetimeImages, default=str), error=error)
            else:
                print("Query failed on Gallery image load.")
                datetime = '1000-04-04 15'
                query1, query2, latestImages, datetimeImages = createquery(datetime)
                return render_template("gallery.html", latestimages=json.dumps(latestImages, default=str), datetimeimages=json.dumps(datetimeImages, default=str), error=error)
        else:
            query1, query2, latestImages, datetimeImages = createquery(datetime)

            if query1 > 0:
                return render_template("gallery.html", latestimages=json.dumps(latestImages, default=str), datetimeimages=json.dumps(datetimeImages, default=str), error=error)
            else:
                print("Query failed on Gallery image load.")
                return render_template("gallery.html", error=error)

    except Exception as e:
        return str(e)


@app.route("/logout/", methods=['GET', 'POST'])
def logout():
    error = ''
    if request.method == 'POST':
        pass
    return render_template("logout.html", error=error)

def createquery(datetime):
    if datetime == "":
        datetime = '2018-04-04 15'
        query = "select * from store_image WHERE date_time BETWEEN '" + datetime + ":00:00' AND '" + datetime + ":59:59' ORDER BY date_time DESC LIMIT 5"
    else:
        query = "select * from store_image WHERE date_time BETWEEN '" + datetime + ":00:00' AND '" + datetime + ":59:59' ORDER BY date_time DESC LIMIT 5"

    dbcursor, conn = db.login_connection()

    query1 = dbcursor.execute("SELECT * FROM store_image ORDER BY date_time DESC LIMIT 5")
    latestImages = []
    columns = [column[0] for column in dbcursor.description]
    for row in dbcursor.fetchall():
        latestImages.append(dict(zip(columns, row)))

    query2 = dbcursor.execute(query)
    datetimeImages = []
    columns = [column[0] for column in dbcursor.description]
    for row in dbcursor.fetchall():
        datetimeImages.append(dict(zip(columns, row)))

    dbcursor.close()
    conn.close()
    gc.collect()
    return query1, query2, latestImages, datetimeImages

if __name__ == "__main__":
    app.run(host="192.168.0.9", port=5000)
    #app.run(host="127.0.0.1", port=5000)


