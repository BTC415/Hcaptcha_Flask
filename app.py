import subprocess
import uuid
import os

from flask import Flask, jsonify, send_from_directory, render_template, request

app = Flask(__name__)
app.debug = True


@app.route("/create-session", methods=["POST", "GET"])
def create_session():
    cpf = request.args.get("cpf","06780432627")
    data_nascimento = request.args.get("data_nascimento","20/05/1983")
    token = str(uuid.uuid4())

    process = subprocess.Popen(
        ["python3", "hcaptcha.py", token, cpf, data_nascimento],
        stdout=subprocess.PIPE,
    )
    return render_template("page.html", token=token)
    return jsonify({"token": token})


@app.route("/download/<upload_id>")
def download(upload_id):
    file_path = f"{upload_id}.txt"
    content = ''
    with open(file_path, "rb") as file:
        content = file.read().decode("utf-8")

    return render_template("page.html", content=content)
    # if os.path.exists(file_path):
    #     return send_from_directory(".", file_path, as_attachment=True)
    # else:
    #     return jsonify({"message": "Please try again later."})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
