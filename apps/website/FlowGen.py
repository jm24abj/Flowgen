from flask import Flask,redirect,url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    css_ = url_for('static', filename='style.css')
    return render_template("index.html", css_path=css_)

if __name__ == "__main__":
    app.run()