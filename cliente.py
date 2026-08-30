import re

class Cliente:
    def __init__(self, nome: str, email: str, cpf: str):
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.__saldo_cupom = 0.0

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor: str):
        if not isinstance(valor, str) or "@" not in valor:
            raise ValueError("O e-mail deve conter o caractere '@'.")
        
        partes = valor.split("@")
        if len(partes) != 2 or not partes[0] or not partes[1]:
            raise ValueError("O e-mail deve conter texto antes e depois do '@'.")
            
        self._email = valor

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, valor: str):
        if not re.match(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', valor):
            raise ValueError("O CPF deve estar no formato 999.999.999-99.")

        numeros = re.sub(r'\D', '', valor)

        if len(set(numeros)) == 1:
            raise ValueError("CPF inválido: sequência de números idênticos.")

        soma1 = sum(int(numeros[i]) * (10 - i) for i in range(9))
        resto1 = (soma1 * 10) % 11
        dv1 = 0 if resto1 == 10 else resto1

        soma2 = sum(int(numeros[i]) * (11 - i) for i in range(10))
        resto2 = (soma2 * 10) % 11
        dv2 = 0 if resto2 == 10 else resto2

        if int(numeros[9]) != dv1 or int(numeros[10]) != dv2:
            raise ValueError("CPF inválido: dígitos verificadores incorretos.")

        self.__cpf = valor

    def get_saldo_cupom(self):
        return self.__saldo_cupom

    def adicionar_cupom(self, valor: float):
        if valor <= 0:
            raise ValueError("O valor do cupom deve ser maior que zero.")
        self.__saldo_cupom += valor

    def __str__(self):

        cpf_numerico = re.sub(r'\D', '', self.__cpf) if hasattr(self, '_Cliente__cpf') else ''
        return f"Cliente: {self.nome} | CPF: {cpf_numerico}"

    def __repr__(self):
        return f"Cliente(nome='{self.nome}', email='{self._email}', cpf='{self.__cpf}')"