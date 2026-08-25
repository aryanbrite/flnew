from flask import Flask, render_template, url_for, redirect, request, session

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")



@app.route("/about")
def about():
    return render_template("about.html")

app.secret_key = "secrectsesstion"

@app.route("/form", methods = ["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form.get("name")
        feedback = request.form.get("feedback")
        internal = request.form.get("internal")

        session["name"] = name
        session["internal"] = internal
        return redirect(url_for("thankyou"))



    return render_template("form.html")

@app.route("/thankyou")
def thankyou():
    if "name" in session and "internal" in session:
        return render_template("thankyou.html")
    else:
        return render_template("error.html")


