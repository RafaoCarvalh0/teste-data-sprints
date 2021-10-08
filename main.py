import dotenv
from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import mysql.connector
import json
import os

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("MYSQL_URI")

db = SQLAlchemy(app)


class usuarios(db.Model):

    id_usuario = db.Column(db.Integer, primary_key=True)
    apelido_usuario = db.Column(db.String(15))
    senha_usuario = db.Column(db.String(32))
    email_usuario = db.Column(db.String(70))
    nome_usuario = db.Column(db.String(100))
    idade_usuario = db.Column(db.Integer)
    endereco_usuario = db.Column(db.String(200))

    def to_json(self):
        return {"id_usuario": self.id_usuario,
                "apelido_usuario": self.apelido_usuario,
                "senha_usuario": self.senha_usuario,
                "email_usuario": self.email_usuario,
                "nome_usuario": self.nome_usuario,
                "endereco_usuario": self.endereco_usuario,
                }


def res_frame(status, res, res_data, message=False):
    body = {}
    body[res] = res_data

    if(message):
        body["message"] = message

    return Response(json.dumps(body), status=status, mimetype="application/json")


@app.route("/signup", methods=["POST"])
def signup():

    ## username, password, email, nomeCompleto, idade, endereco
    body = request.get_json()

    try:
        usuario = usuarios(
            apelido_usuario=body["username"],
            email_usuario=body["email"]
        )

        db.session.add(usuario)
        db.session.commit()
        return res_frame(201, "usuario", usuario.to_json(), "Usuário Criado")

    except Exception as err:
        print(err)
        return res_frame(400, "", {}, "Erro ao Criar Usuário")


@app.route("/signin", methods=["POST"])
def signin():

    body = request.get_json()

    try:
        user_exists = usuarios.query.filter_by(
            email_usuario=body['email'],
            senha_usuario=body['senha']
        ).first()

        return res_frame(201, "usuario", user_exists.to_json(), "Usuário Existe")

    except Exception as err:
        print(err)
        if user_exists == None:
            return res_frame(400, "usuario", {}, "Usuário Inexistente")
        else:
            return res_frame(400, "", {}, "Erro ao Realizar Login")


app.run(host='localhost', port=8000, debug=True)
