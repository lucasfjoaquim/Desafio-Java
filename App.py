from flask import Flask, request, jsonify
from datetime import datetime, timedelta
from usuario import Usuario  # Importando a classe Usuario do arquivo usuario.py
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'super-secret'  # Chave secreta para assinar os tokens JWT
jwt = JWTManager(app)

# Lista para armazenar os usuários criados (simulando um banco de dados)
usuarios = []
ids = []


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    senha = data.get('senha')
    usuario_logado = None

    # Verifica se o email e a senha correspondem a um usuário existente
    for usuario in usuarios:
        if usuario.email == email and usuario.senha == senha:
            # Cria um token de acesso JWT válido por 1 hora
            expires = timedelta(hours=1)
            access_token = create_access_token(identity=email, expires_delta=expires)
            return jsonify({"jwt_token": access_token,
                            "user_id": usuario.user_id,
                            "email": usuario.email,
                            "nome": usuario.nome_completo,
                            "data_registro": usuario.data_registro}), 200


    return jsonify({'mensagem': 'E-mail ou senha inválidos'}), 401


@app.route('/usuarios', methods=['POST'])
def criar_usuario():
    data = request.get_json()
    if not ids:
        user_id = 0
        ids.append(user_id)
    else:
        print(ids[-1:][0])
        user_id = ids[-1:][0] + 1
        ids.append(user_id)

    lista_emails = []
    for usuario in usuarios:
        lista_emails.append(usuario.email)

    if data['email'] not in lista_emails:

        try:
            novo_usuario = Usuario(
                user_id= user_id,
                nome_completo=data['nome_completo'],
                email=data['email'],
                senha=data['senha'],
                data_registro=datetime.now()
            )
            usuarios.append(novo_usuario)
            for usuario in usuarios:
                print(usuario)
            return jsonify({"user_id": user_id,
                            "email": data['email'],
                            "nome": data['nome_completo'],
                            "data_registro" : datetime.now()}), 201
        except KeyError:
            return jsonify({'mensagem': 'Campos inválidos no corpo da requisição.'}), 400
        except ValueError as e:
            return jsonify({'mensagem': str(e)}), 400
    else:
        return jsonify({'mensagem': 'Usuario ja cadastrado.'}), 400


@app.route('/usuarios', methods=['GET'])
@jwt_required()
def recurso_protegido():
    current_user = get_jwt_identity()
    user_array = []
    for usuario in usuarios:
        user_array.append({"id": usuario.user_id,
                           "nome": usuario.nome_completo,
                           "email": usuario.email,
                           "data de cadastro": usuario.data_registro})

    response_dict = {"user_list": user_array}
    return jsonify(response_dict)



if __name__ == '__main__':
    app.run(debug=True)