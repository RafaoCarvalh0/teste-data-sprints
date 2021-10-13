from services import usuario_service

def create_usuario(usuario):
    try:

        err = []
        if usuario["username"] == "":
            err.append("Apelido")

        if usuario["senha"] == "" :
            err.append("Senha")
        
        if usuario["email"] == "":
            err.append("Email")
        
        if usuario["nome_completo"] == "":
            err.append("Nome Completo")
            

        if len(err) > 0:
            return [400, "Informações necessárias", err, "Erro"]
        else:
            return usuario_service.create_usuario(usuario)

    except Exception:

        return [400, "", {}, "Requisição inválida"]


def login_usuario(usuario):
    try:

        err=[]
        if usuario["email"] == "":
            err.append("Apelido")

        if usuario["senha"] == "":
            err.append("Senha")


        if len(err) > 0:
            return [400, "Informações necessárias", err, "Erro"]
        else:
            return usuario_service.login_usuario(usuario)
    
    except Exception:
        
        return [400, "", {}, "Requisição inválida"]



