from flask import Flask, render_template
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route("/")
def home():
    return "Hello, Flask! 🚀"

if __name__ == "__main__":
    app.run()