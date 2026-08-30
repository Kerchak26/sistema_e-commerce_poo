class Produto:
    def __init__(self, nome_produto: str,categoria:str, preco: float):
        self.nome_produto = nome_produto  # Atributo público
        self._categoria = categoria # Atributo "protegido"          
        if preco > 0:
         self.__preco = preco
        else:
         raise ValueError('Valor Inválido!')
                                  
    @property
    def preco(self):
       return self.__preco
      
    @preco.setter
    def preco(self,preco):
     if preco > 0:
         self.__preco = preco
     else:
      raise ValueError("O preço deve ser maior que zero")    

    def __repr__(self):
     formato = f"Produto(nome='{self.nome_produto}', " + \
              f"categoria='{self._categoria}', " + \
              f"preco={self.__preco})"
     return formato

    def __str__(self):
     return f"{self.nome_produto} ({self._categoria}) - R$ {self.__preco:.2f}"
