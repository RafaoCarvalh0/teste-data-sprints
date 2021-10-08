CREATE TABLE usuarios(
	id_usuario SERIAL PRIMARY KEY,
    apelido_usuario VARCHAR(15),
    senha_usuario VARCHAR(32),
    email_usuario VARCHAR(70),
    nome_usuario VARCHAR(100),
    idade_usuario INT,
    endereco_usuario VARCHAR(200)
)