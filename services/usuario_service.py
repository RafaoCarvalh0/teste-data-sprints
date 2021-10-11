from repositories import usuario_repository

def create_usuario(usuario):
    try:
        return usuario_repository.create_usuario(usuario)
    except Exception as err:
        print(err)
        return [500, "", {}, "Erro Interno"]


def login_usuario(usuario):
    try:
        if usuario_repository.get_usuario(usuario) == None:
            return [404, "", {}, "Usuário não encontrado"]
        else:
            return usuario_repository.login_usuario(usuario)

    except Exception:
        return [500, "", {}, "Erro Interno"]

