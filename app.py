import subprocess
import uuid

from flask import (
    Flask,
    jsonify,
    send_from_directory,
)

app = Flask(__name__)
app.debug = True


@app.route("/create-session", methods=["POST", "GET"])
def create_session():
    token = str(uuid.uuid4())

    process = subprocess.Popen(
        ["python", "hcaptcha.py", token],
        stdout=subprocess.PIPE,
    )
    return jsonify({"token": token})


@app.route("/download/<upload_id>")
def download(upload_id):
    # return send_file(BytesIO(upload.data), download_name=f'{upload_id}.txt', as_attachment=True )
    return send_from_directory(".", f"{upload_id}.txt", as_attachment=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
