from datetime import datetime


class Usuario:
    def __init__(self, user_id, nome_completo, email, senha, data_registro):
        self.user_id = user_id
        self.set_nome_completo(nome_completo)
        self.set_email(email)
        self.set_senha(senha)
        self.data_registro = data_registro

    def set_nome_completo(self, nome_completo):
        if len(nome_completo) > 0:
            self.nome_completo = nome_completo
        else:
            raise ValueError("Nome completo não pode estar vazio.")

    def set_email(self, email):
        # Verifica se o email possui um formato válido
        if "@" in email and "." in email:
            self.email = email
        else:
            raise ValueError("E-mail inválido.")

    def set_senha(self, senha):
        # Verifica se a senha tem pelo menos um caractere maiúsculo e um dígito
        if any(char.isupper() for char in senha) and any(char.isdigit() for char in senha):
            self.senha = senha
        else:
            raise ValueError("A senha deve conter pelo menos um caractere maiúsculo e um dígito.")

    def __str__(self):
        return f"Usuário: {self.nome_completo}\nID: {self.user_id}\nE-mail: {self.email}\nData de Registro: {self.data_registro}"



if __name__ == "__main__":
    try:
        usuario1 = Usuario(1, "João Silva", "joao@example.com", "Senha123", datetime.now())
        print(usuario1)
    except ValueError as e:
        print(f"Erro ao criar usuário: {e}")