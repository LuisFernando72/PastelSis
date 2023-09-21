from flask import Flask, session, render_template

app = Flask(__name__)


@app.route("/")
def root():
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)