# 1o Trabalho de Programação Orientada a Objetos
# Integrantes:
#   Caio Eduardo de Carvalho
#   Kauã Queiroga Oliveira André
#   Luenmar Briani Venditti

"""Script de homologação do sistema de e-commerce.

Executa, na ordem, as 4 etapas previstas no roteiro de testes do enunciado.
"""

from produto import Produto
from cliente import Cliente
from carrinho import CarrinhoDeCompras


def titulo(texto: str):
    print()
    print("=" * 60)
    print(texto)
    print("=" * 60)


# ---------------------------------------------------------------------------
# ETAPA 1 - Instanciação e inspeção de representação (__str__ e __repr__)
# ---------------------------------------------------------------------------
titulo("ETAPA 1 - INSTANCIACAO E REPRESENTACAO (__str__ / __repr__)")

p1 = Produto("Camiseta", "Vestuário", 49.90)
p2 = Produto("Fone Bluetooth", "Eletrônicos", 249.90)
p3 = Produto("Caneca Térmica", "Utilidades", 75.00)

# Obs.: o CPF '123.456.789-01' citado no enunciado é reprovado pelo próprio
# algoritmo de dígitos verificadores (o DV2 correto seria 9, não 1), por isso
# utilizamos '123.456.789-09'.
cliente = Cliente("Maria Silva", "maria@email.com", "123.456.789-09")

print("--- Saida do __str__ (amigavel ao cliente) ---")
for produto in (p1, p2, p3):
    print(produto)
print(cliente)

print()
print("--- Saida do __repr__ (tecnica, para depuracao) ---")
for produto in (p1, p2, p3):
    print(repr(produto))
print(repr(cliente))


# ---------------------------------------------------------------------------
# ETAPA 2 - Validações e captura de exceções (try/except ValueError)
# ---------------------------------------------------------------------------
titulo("ETAPA 2 - VALIDACOES E CAPTURA DE ValueError")

print("--- Preco nulo ou negativo ---")
try:
    p1.preco = -10.0
except ValueError as e:
    print(f"ValueError capturado: {e}")

try:
    p1.preco = 0
except ValueError as e:
    print(f"ValueError capturado: {e}")

print(f"Preco preservado apos as tentativas invalidas: R$ {p1.preco:.2f}")

print()
print("--- CPF invalido ---")
for cpf_invalido in ("1234", "abc.def.ghi-jk", "111.111.111-11", "123.456.789-00"):
    try:
        cliente.cpf = cpf_invalido
    except ValueError as e:
        print(f"CPF {cpf_invalido!r} -> ValueError: {e}")

print()
print("--- E-mail invalido ---")
for email_invalido in ("mariaemail.com", "@email.com", "maria@"):
    try:
        cliente.email = email_invalido
    except ValueError as e:
        print(f"E-mail {email_invalido!r} -> ValueError: {e}")

print()
print("--- Cupom com valor invalido ---")
try:
    cliente.adicionar_cupom(-5.0)
except ValueError as e:
    print(f"ValueError capturado: {e}")

print()
print(f"Dados do cliente preservados: {cliente!r}")


# ---------------------------------------------------------------------------
# ETAPA 3 - Modificadores de visibilidade e name mangling
# ---------------------------------------------------------------------------
titulo("ETAPA 3 - VISIBILIDADE E NAME MANGLING")

print("--- Atributo PRIVADO: acesso direto gera AttributeError ---")
try:
    print(p1.__preco)
except AttributeError as e:
    print(f"p1.__preco -> AttributeError: {e}")

try:
    print(cliente.__cpf)
except AttributeError as e:
    print(f"cliente.__cpf -> AttributeError: {e}")

# O prefixo __ aciona o name mangling: dentro da classe, o interpretador
# renomeia o atributo para _NomeDaClasse__atributo. Por isso o nome '__preco'
# simplesmente não existe fora da classe.
print(f"Acesso pelo nome real (p1._Produto__preco): {p1._Produto__preco}")
print(f"Forma correta de leitura, via @property (p1.preco): {p1.preco}")

print()
print("--- Atributo PROTEGIDO: acesso permitido pelo Python ---")
print(f"p1._categoria = {p1._categoria}")
# O Python PERMITE esse acesso porque o underscore simples é apenas uma
# CONVENÇÃO entre desenvolvedores, sinalizando "uso interno da classe". Não há
# nenhum mecanismo da linguagem que bloqueie a leitura ou a escrita: diferente
# do __ (que sofre name mangling), o _ não altera o nome do atributo. Trata-se,
# portanto, de um acordo de boas práticas, e não de uma restrição técnica.
print(f"cliente._email = {cliente._email}")


# ---------------------------------------------------------------------------
# ETAPA 4 - Fluxo de carrinho e composição
# ---------------------------------------------------------------------------
titulo("ETAPA 4 - FLUXO DE CARRINHO E COMPOSICAO")

# Composição: o carrinho recebe a instância de Cliente e agrega objetos Produto.
carrinho = CarrinhoDeCompras(cliente)
carrinho.adicionar_produto(p1)
carrinho.adicionar_produto(p2)
carrinho.adicionar_produto(p3)

print("--- Itens do carrinho (listar_itens) ---")
carrinho.listar_itens()

print()
print(f"Total (via @property): R$ {carrinho.total:.2f}")
print(f"__str__ : {carrinho}")
print(f"__repr__: {carrinho!r}")

print()
print("--- Removendo um produto ---")
carrinho.remover_produto(p3)
print(f"Apos remover '{p3.nome}': {carrinho}")
carrinho.adicionar_produto(p3)
print(f"Produto readicionado    : {carrinho}")

print()
print("--- Saldo de cupons do cliente (encapsulamento tradicional) ---")
print(f"Saldo inicial: R$ {cliente.get_saldo_cupom():.2f}")
cliente.adicionar_cupom(50.0)
cliente.adicionar_cupom(25.50)
print(f"Saldo apos adicionar R$ 50.00 e R$ 25.50: R$ {cliente.get_saldo_cupom():.2f}")

print()
print("--- Fechamento do pedido ---")
desconto = min(cliente.get_saldo_cupom(), carrinho.total)
valor_final = carrinho.total - desconto
print(f"Subtotal        : R$ {carrinho.total:.2f}")
print(f"Desconto (cupom): R$ {desconto:.2f}")
print(f"Valor a pagar   : R$ {valor_final:.2f}")

print()
print("Homologacao concluida com sucesso.")
