from flask import Flask, request, send_file
from flask_cors import CORS
from rembg import remove
import io

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return "ACP Remove BG API Running"


@app.route("/remove-bg", methods=["POST"])
def remove_bg():

    image = request.files["image"]

    output = remove(image.read())

    return send_file(
        io.BytesIO(output),
        mimetype="image/png"
    )


if __name__ == "__main__":
    app.run()
