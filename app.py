from flask import Flask, render_template, render_template, request

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def main():
    if request.method == "GET":
        return render_template("basic.html", Error = "Enter Username and Password")
    elif request.method == "POST":
        uname = request.form["username"]
        pword = request.form["password"]
        if uname != "admin" and pword == "chickens":
            return render_template("basic.html", Error= "Username and Password not found")
        else:
            return render_template("main_page.html")

if __name__ == "__main__":
    app.run(host = "0.0.0.0")