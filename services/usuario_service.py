from repositories import usuario_repository

def create_usuario(usuario):
    try:

        err = []
        data = usuario_repository.get_usuario(usuario)
        if data:
            if data.email_usuario == usuario["email"]:
                err.append("Email")

            if data.apelido_usuario == usuario["username"]:
                err.append("Apelido")

            return [400, "Dados em uso", err, "Duplicidade"]
        else:
            return usuario_repository.create_usuario(usuario)

    except Exception:

        return [500, "", {}, "Erro Interno"]


def login_usuario(usuario):
    try:

        bearer = usuario_repository.login_usuario(usuario)

        if bearer == "'username'":
            return [404, "", {}, "Usuário não encontrado"]
        else:
            return bearer

    except Exception:
        
        return [500, "", {}, "Erro Interno"]

