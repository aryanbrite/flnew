from flask import Flask, redirect, render_template, request, url_for, session

app = Flask(__name__)

app.secret_key = 'supersession'



@app.route("/", methods = ["POST", "GET"])
def login():

    if "user" in session:
        return redirect(url_for("welcome"))

    else:
        username = request.form.get("username")
        password = request.form.get("password")
        user = {"aryan": '123', "kunal": '2008', "priya": '2008'}

        if username in user and password == user[username]:
            session["user"] = username
            return redirect(url_for('welcome'))
    return render_template("login.html")
    


@app.route("/welcome")
def welcome():
    if "user" in session:
        return render_template("welcome.html")


app.run()


