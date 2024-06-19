from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'Database/main_db.db')

db = SQLAlchemy(app)

migrate = Migrate(app,db)


class Vartotojas(db.Model):
    __tablename__ = "Users"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)

    def __init__(self, name, age):
        self.name = name
        self.age = age



@app.route("/")
def home():
    error = request.args.get('error')
    return render_template("index.html", err=error)

@app.route("/Greeting/<name>/<lastName>")
def greet(name, lastName):
    return "Sveiki, " + name + lastName

@app.route("/Bye/<name>")
def bye(name):
    return "Bye" + name

@app.route("/Okay")
def ok():
    return "Okay"

@app.route("/NameVeryOldName", methods = ["GET"])
def old_enter_name():
    url = url_for('home', error="Very bad error")
    return redirect(url)

@app.route("/NameVeryGoodName", methods = ["GET"])
def enter_name():
    return render_template("name_form.html")

@app.route("/CreateUser", methods = ["GET"])
def create_get():
    return render_template("Create_User.html")


@app.route("/CreateUser", methods = ["POST"])
def create_post():
    try:
        vardas = request.form["firstName"]
        age = request.form["age"]
        user = Vartotojas(vardas,age)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("home", error="Everything was okay"))
    except:
        return redirect(url_for("home", error="User was not inserted"))



@app.route("/Name_Submit", methods = ["POST"])
def name_print():
    vardas = request.form["firstName"]
    print(f"Hello your name is: {vardas}")
    return ""

if __name__ == "__main__":
    app.run(debug=True)