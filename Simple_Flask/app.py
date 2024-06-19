from flask import Flask, render_template, request, redirect, url_for

print(__name__)

app = Flask(__name__)

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

@app.route("/Name_Submit", methods = ["POST"])
def name_print():
    vardas = request.form["firstName"]
    print(f"Hello your name is: {vardas}")
    return ""


app.run(debug=True)