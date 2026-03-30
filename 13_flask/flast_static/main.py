from flask import Flask, render_template, request, jsonify, flash

# app = Flask(__name__,static_url_path="/public") # This how you change static url path
app = Flask(
    __name__, static_folder="assets"
)  # This is how you change static folder location


@app.route("/", methods=["GET", "POST"])
def home():
    """print(request.method)
    print(request.form)"""
    if request.method == "POST":
        with open("file.txt", "w") as f:
            f.write(
                f"The name is {request.form['name']} and email is {request.form['email']}"
            )
        return render_template("home.html")
    else:
        return render_template("home.html")


@app.route("/services")
def services():
    marks = {
        "John": 45,
        "Saurabh": 99,
        "Mark": 45,
        "Jeff": 67,
        "Alexa": 90,
        "Lily": 100,
    }
    return render_template("services.html", marks=marks)


@app.route("/about")
def about():
    # name = "Yash"
    # token = 67000
    name = request.args["name"]
    token = request.args["token"]
    return render_template("about.html", name=name, token=token)


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/jsondata")
def json():
    marks = {"Harry": 56, "Rohan": 67, "Aakash": 78, "Shubham": 100, "Reena": 67}
    return jsonify(marks)


app.run(port=8000, debug=True)
