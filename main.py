from flask import Flask, Response, request
from dotenv import load_dotenv
from repositories.mysql_db import db
from controllers import usuarios_controller
import json
import os

load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("MYSQL_URI")

db.init_app(app)


def res_frame(status, res, res_data, message=False):
    body = {}
    body[res] = res_data

    if(message):
        body["message"] = message

    return Response(json.dumps(body), status=status, mimetype="application/json")



@app.route("/signup", methods=["POST"])
def signup():
    res = usuarios_controller.create_usuario(request.get_json())
    return res_frame(res[0], res[1], res[2], res[3])



@app.route("/signin", methods=["POST"])
def signin():
    res = usuarios_controller.login_usuario(request.get_json())
    return res_frame(res[0], res[1], res[2], res[3])


app.run(host="localhost", port=8000, debug=True)
