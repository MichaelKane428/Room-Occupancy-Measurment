'''
    Michael Kane 2017

    Student No: C14402048
    course: DT211C
    Date: 12/11/2017

    Introduction:

    Step-by-Step:

    OverView: This

    References:
    https://gist.github.com/yoavram/4351498
    https://www.youtube.com/watch?v=T1ZVyY1LWOg
    https://pymotw.com/2/gc/
    https://www.youtube.com/watch?v=PiphizBQJho&index=16&list=PLQVvvaa0QuDc_owjTbIY4rbgXOFkUYOUB
    https://www.youtube.com/playlist?list=PLQVvvaa0QuDc_owjTbIY4rbgXOFkUYOUB
    https://stackoverflow.com/questions/27539309/how-do-i-create-a-link-to-another-html-page
'''
import os
from flask import Flask, render_template, request, url_for, flash, session, redirect
import gc
from flask_cors import CORS
from FYP import databaseconnection as db

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
        if file and allowedFile(file.filename):
            filename = file.filename
            print(filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
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


@app.route("/gallery/", methods=['GET'])
def gallery():
    error = ''
    return render_template("gallery.html", error=error)


@app.route("/logout/", methods=['GET', 'POST'])
def logout():
    error = ''
    if request.method == 'POST':
        pass
    return render_template("logout.html", error=error)

if __name__ == "__main__":
    app.run(host="192.168.0.9", port=5000)


