# Processo Seletivo DataSprints (Python)

## Preparando o ambiente e utilizando a API.

### Versão necessária: Python 3.9.7

#### Em seu ambiente virutal

Na raiz do projeto, execute o seguinte comando para instalar as dependências necessárias:
```bash
pip install -r requirements.txt
```

Na raiz do projeto, execute o seguinte comando para gerar o arquivo key.key
```python
python generate.key.py

# NÃO EXCLUA O ARQUIVO GERADO
```
Este arquivo contém a chave responsável por codificar e decodificar as senhas criadas pela API. Não exclua.


## 1 - Banco de Dados (MySql)

Com o ambiente configurado, crie um novo schema em seu MySql e restaure o arquivo "db-structure.sql" localizado na raiz do projeto

### Restaurando o  Banco

#### Restore MySql Linux:
Dentro da pasta raiz do projeto, execute:
```bash
mysql -u [usuario_do_Banco] -p [nome_do_banco] < db-structure.sql
```

#### Restore MySql Windows:
Utilizando o cmd, navegue até a pasta bin do MySql e execute:
```bash
mysql -u [usuario_do_Banco] -p [nome_do_banco] < "[diretorio_raiz_do_projeto]/db-structure.sql"
```
#### Restore Manual (em caso de erros):
```
Abra o arquivo "db-structure.sql" em seu MySql Workbench e execute a query
```


## 2 - Variáveis de ambiente

No diretório Raiz do projeto, crie um arquvio ".env" e edite-o da seguinte forma:
```dotenv
DB_USER=[usuario_do_bd]
DB_PASS=[senha_do_bd]
DB_IP=[endereco_do_bd]
DB_PORT=[porta_do_bd]
DB_NAME=[nome_do_bd]

API_PORT=[porta_da_api]

MYSQL_URI=mysql://${DB_USER}:${DB_PASS}@${DB_IP}:${DB_PORT}/${DB_NAME}

SECRET_SHH=[crie_uma_chave_secreta_para_uso_do_JWT]
```
Salve o arquivo.

## 3 - Executando a API
Na pasta raiz do projeto execute:
```python
python main.py
```

Exemplo de output caso todas as configurações estejam corretas:
```python
 * Serving Flask app 'main' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 582-393-193
 * Running on http://localhost:8000/ (Press CTRL+C to quit)
```
---
# Rotas

## 1 - Usuários

### [POST] - Cadastrar um novo usuário.
```python
{{url-base}}/signup
```
```json

{
	"username":"foo",
	"email":"foo@bar.com",
	"senha":"foobar123",
	"nome_completo":"Foo Bar 123",
	"endereco":"Foo Bar 123"
}
```
### [POST] - Login de um usuário
```python
{{url-base}}/signin
```
```json

{
	"email":"foo@bar.com",
	"senha":"foobar123"
}
```

