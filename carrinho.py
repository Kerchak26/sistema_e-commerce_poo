from cliente import Cliente
from produto import Produto


class CarrinhoDeCompras:
    def __init__(self, cliente: Cliente):
        if not isinstance(cliente, Cliente):
            raise TypeError("O carrinho exige uma instância válida de Cliente.")

        self.cliente = cliente  # Atributo público (composição com Cliente)
        self.__itens = []  # Atributo privado: lista de objetos Produto

    def adicionar_produto(self, produto: Produto):
        if not isinstance(produto, Produto):
            raise TypeError("Só é possível adicionar instâncias de Produto.")
        self.__itens.append(produto)

    def remover_produto(self, produto: Produto):
        if produto in self.__itens:
            self.__itens.remove(produto)

    @property
    def total(self):
        # Percorre a lista privada somando o preço de cada produto.
        return sum(produto.preco for produto in self.__itens)

    def listar_itens(self):
        if not self.__itens:
            print("O carrinho está vazio.")
            return

        for produto in self.__itens:
            print(f"- {produto}")  # Usa o __str__ de Produto

    def __str__(self):
        return (f"Carrinho de {self.cliente.nome} | "
                f"{len(self.__itens)} item(ns) | "
                f"Total: R$ {self.total:.2f}")

    def __repr__(self):
        return (f"CarrinhoDeCompras(cliente={self.cliente!r}, "
                f"total_itens={len(self.__itens)})")
