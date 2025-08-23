from flask import Flask, render_template

app = Flask(__name__)

@app.get("/")
def home():
    # This will render templates/index.html
    return render_template("index.html")

if __name__ == "__main__":
    # Local dev
    app.run(host="0.0.0.0", port=5000)
