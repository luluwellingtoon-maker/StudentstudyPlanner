from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")

def home():

    return render_template("index.html")

@app.route("/result", methods=["POST"])

def result():

    name = request.form.get("name")

    subject = request.form.get("subject")

    hours = request.form.get("hours")

    return render_template(

        "result.html",

        name=name,

        subject=subject,

        hours=hours

    )
if __name__ == "__main__":

    app.run(debug=True)