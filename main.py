from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import jwt
import datetime
import json
import os

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("MYSQL_URI")
app.config['SECRET_KEY'] = os.environ.get('SECRET_SHH')

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
        return {
                "id_usuario": self.id_usuario,
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

    body = request.get_json()

    try:
        usuario = usuarios(
            apelido_usuario=body["username"],
            senha_usuario=body["senha"],
            email_usuario=body["email"],
            nome_usuario=body["nome_completo"],
            endereco_usuario=body["endereco"]
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
        usuario = usuarios.query.filter_by(
            email_usuario=body['email'],
            senha_usuario=body['senha']
        ).first()


        if usuario.email_usuario and usuario.senha_usuario:
            token = jwt.encode({
                'id':usuario.id_usuario,
                'username':usuario.apelido_usuario,
                'email':usuario.email_usuario,
                'nome_completo':usuario.nome_usuario,
                'idade':usuario.idade_usuario,
                'endereco':usuario.endereco_usuario,
                'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=30), 
            },
            app.config['SECRET_KEY']
            )

        return res_frame(200, "token", token, "Acesso Concedido")

    except Exception as err:
        print(err)
        if usuario == None:
            return res_frame(406, "", {}, "Usuário Inexistente")
        else:
            return res_frame(400, "", {}, "Erro ao Realizar Login")


app.run(host='localhost', port=8000, debug=True)
