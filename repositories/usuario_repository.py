from models.usuarios_model import usuarios, db
from cryptography.fernet import Fernet
import jwt
import datetime
import os

global f
key = open("key.key", "rb").read()
f = Fernet(key)


def create_usuario(usuario):
    try:
        
        data = usuarios(
            apelido_usuario=usuario["username"],
            senha_usuario=f.encrypt(usuario["senha"].encode()),
            email_usuario=usuario["email"],
            nome_usuario=usuario["nome_completo"],
            endereco_usuario=usuario["endereco"]
        )

        db.session.add(data)
        db.session.commit()
        del usuario["senha"]
        return [201, "usuario", usuario, "Usuário Criado"]

    except Exception as err:

        print(err)
        return [500, "", {}, "Erro Interno"]



def get_usuario(data):
    try:

        usuario = usuarios.query.filter_by(
                email_usuario=data["email"]
            ).first()

        if not usuario:
            usuario = usuarios.query.filter_by(
                apelido_usuario=data["username"]
            ).first()

        return usuario

    except Exception as err:
        
        if str(err) == "'username'":
            return str(err)
        else:
            return [500, "", {}, "Erro interno"]



def login_usuario(data):
    try:
        usuario = get_usuario(data)

        if usuario == "'username'":
            return usuario

        if check_pwd(data["senha"], usuario.senha_usuario):
            token = jwt.encode({
                "id":usuario.id_usuario,
                "username":usuario.apelido_usuario,
                "email":usuario.email_usuario,
                "nome_completo":usuario.nome_usuario,
                "idade":usuario.idade_usuario,
                "endereco":usuario.endereco_usuario,
                "exp":datetime.datetime.utcnow() + datetime.timedelta(minutes=30), 
            },
            os.environ.get("SECRET_SHH")
            )

            return [200, "token", token, "Acesso Concedido."]
            
        else:
            return [401, "", {}, "Credenciais inválidas."]

    except Exception:
        return [500, "", {}, "Erro interno"]



def check_pwd(req_pwd, usr_pwd):
    usr_pwd = usr_pwd.encode()
    pwd = f.decrypt(usr_pwd)

    if req_pwd == pwd.decode():
        return True
    else:
        return False

