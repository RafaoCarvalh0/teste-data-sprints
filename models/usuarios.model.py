from flask_sqlalchemy import SQLAlchemy

app = ''

db = SQLAlchemy(app)

class usuarios(db.model):
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

