# from flask import Flask
from app import create_app
from flask import make_response, jsonify


app = create_app()


@app.route("/")
def home():
    return make_response(jsonify({"status": 200, "message": "okay"}))


if __name__ == "__main__":
    app.run()
