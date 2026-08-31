class Produto:
    def __init__(self, nome: str, categoria: str, preco: float):
        self.nome = nome  # Atributo público
        self._categoria = categoria  # Atributo "protegido"
        self.preco = preco  # Delega a validação ao @preco.setter

    @property
    def preco(self):
        return self.__preco  # Atributo privado

    @preco.setter
    def preco(self, preco):
        if preco <= 0:
            raise ValueError("O preço deve ser maior que zero.")
        self.__preco = preco

    def __repr__(self):
        return (f"Produto(nome='{self.nome}', "
                f"categoria='{self._categoria}', "
                f"preco={self.__preco})")

    def __str__(self):
        return f"{self.nome} ({self._categoria}) - R$ {self.__preco:.2f}"
