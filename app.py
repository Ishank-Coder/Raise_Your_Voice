from flask import Flask, redirect, render_template, url_for
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template( "home.html")

# @app.route("/<name>")
# def user(name):
#     return f"Hello{name}"

@app.route("/requestRegister.html",methods=["GET", "POST"])
def registerReq():
    return render_template("requestRegister.html")

@app.route("/admin")
def admin():
    return redirect(url_for("home"))

if __name__ == '__main__':
    app.run()


