from flask import Flask

app = Flask(__name__)


@app.route("/info")
def data():
    return ("Hello Learn Local")


if __name__ =="__main__":
    app.run(debug=True)