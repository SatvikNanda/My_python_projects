import os
from flask import Flask, render_template

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Create the Flask app and specify the templates folder
app = Flask(__name__, template_folder=os.path.join(current_dir, 'templates'))

@app.route("/")
def home():
    return render_template("demo.html")

@app.route("/about/")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
