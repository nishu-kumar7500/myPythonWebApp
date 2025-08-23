from flask import Flask

app = Flask(__name__)

@app.get("/")
def root():
    return {"message": "Hello from Flask on Azure!"}, 200

if __name__ == "__main__":
    # Local dev only; Azure will use gunicorn
    app.run(host="0.0.0.0", port=5000)
