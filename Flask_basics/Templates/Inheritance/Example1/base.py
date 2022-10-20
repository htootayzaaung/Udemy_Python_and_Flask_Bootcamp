from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("home.html")

@app.route("/cat/<name>")
def pup_name(name):
    return render_template("cat.html", name = name)

if __name__ == "__main__":
    app.run(debug = True)
