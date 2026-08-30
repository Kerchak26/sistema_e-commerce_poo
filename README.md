# Sistema de E-Commerce — 1º Trabalho de Programação Orientada a Objetos

Protótipo da **camada de negócios** de um e-commerce, desenvolvido em Python com foco em
**encapsulamento**, **propriedades ativas com validação** e **composição de objetos** — sem uso de herança.

- **Disciplina:** Object-Driven Development (Programação Orientada a Objetos)
- **Professor:** Lucio Nunes de Lira
- **Semestre letivo:** 2026-2
- **Formato:** atividade obrigatoriamente em trio

---

## Sumário

- [Objetivos pedagógicos](#objetivos-pedagógicos)
- [Estrutura do projeto](#estrutura-do-projeto)
- [Como executar](#como-executar)
- [Especificação dos módulos](#especificação-dos-módulos)
  - [produto.py — Integrante 1](#produtopy--integrante-1)
  - [cliente.py — Integrante 2](#clientepy--integrante-2)
  - [carrinho.py — Integrante 3](#carrinhopy--integrante-3)
- [Roteiro de homologação (main.py)](#roteiro-de-homologação-mainpy)
- [Algoritmo de validação de CPF](#algoritmo-de-validação-de-cpf)
- [Matriz de avaliação](#matriz-de-avaliação)
- [Entrega](#entrega)
- [Integrantes](#integrantes)

---

## Objetivos pedagógicos

Tópicos obrigatórios avaliados nesta atividade:

- Criação de classes e instanciação de objetos em **arquivos/módulos separados**;
- Uso dos níveis de acesso: **público**, **protegido** (convenção `_`) e **privado** (mecanismo `__`, *name mangling*);
- Uso de **getters/setters tradicionais** e da sintaxe pythônica com `@property` e `@<nome>.setter`;
- **Tratamento defensivo**: verificação de regras de negócio e disparo de `ValueError` nos setters;
- Implementação dos métodos *dunder* de representação em string: `__str__` e `__repr__`;
- **Composição de objetos** (agregação de instâncias no carrinho de compras).

---

## Estrutura do projeto

```
atividade1_poo/
├── produto.py    # Classe Produto            (Integrante 1)
├── cliente.py    # Classe Cliente            (Integrante 2)
├── carrinho.py   # Classe CarrinhoDeCompras  (Integrante 3)
├── main.py       # Script de homologação / testes
└── README.md
```

O trabalho é dividido equitativamente: cada integrante é responsável por desenvolver a classe do
seu módulo correspondente. O `main.py` é a unificação do sistema, feita pelo trio.

---

## Como executar

Requisitos: **Python 3.10+** (sem dependências externas).

```bash
python main.py
```

---

## Especificação dos módulos

### `produto.py` — Integrante 1

**Responsabilidade:** modelar o item comercializado, garantindo integridade de valores econômicos.

#### Atributos

| Atributo | Visibilidade | Tipo | Descrição |
|---|---|---|---|
| `nome` | público | `str` | Nome do produto |
| `_categoria` | protegido | `str` | Segmento do produto (ex.: `"Vestuário"`, `"Eletrônicos"`) |
| `__preco` | privado | `float` | Preço unitário do item |

#### Propriedades e regras

- Propriedade `preco` implementada com `@property` e `@preco.setter`.
- O setter exige **preço positivo** (`preco > 0`). Caso contrário, dispara `ValueError` com
  mensagem explicativa.

#### Métodos especiais

| Método | Retorno esperado |
|---|---|
| `__str__` | `Camiseta (Vestuário) - R$ 49.90` |
| `__repr__` | `Produto(nome='Camiseta', categoria='Vestuário', preco=49.9)` |

---

### `cliente.py` — Integrante 2

**Responsabilidade:** modelar o comprador do sistema, com validação rigorosa de dados cadastrais.

#### Atributos

| Atributo | Visibilidade | Tipo | Descrição |
|---|---|---|---|
| `nome` | público | `str` | Nome completo |
| `_email` | protegido | `str` | E-mail do cliente |
| `__cpf` | privado | `str` | CPF no formato `999.999.999-99` |
| `__saldo_cupom` | privado | `float` | Saldo acumulado em cupons (inicia em `0.0`) |

#### Propriedades e métodos

- **`email`** — `@property` / `@email.setter`. Exige a presença do caractere `"@"` **e** de
  texto antes e depois dele; dispara `ValueError` caso contrário.
- **`cpf`** — `@property` / `@cpf.setter`. Valida a máscara `999.999.999-99`
  (14 caracteres) e os dígitos verificadores; lança `ValueError` se inválido.
  Veja [Algoritmo de validação de CPF](#algoritmo-de-validação-de-cpf).
- **Encapsulamento tradicional** — métodos `get_saldo_cupom()` e `adicionar_cupom(valor)`.
  O método de adição valida `valor > 0` e dispara `ValueError` se `valor <= 0`.

#### Métodos especiais

| Método | Retorno esperado |
|---|---|
| `__str__` | `Cliente: Maria Silva \| CPF: 12345678901` |
| `__repr__` | `Cliente(nome='Maria Silva', email='maria@email.com', cpf='123.456.789-01')` |

---

### `carrinho.py` — Integrante 3

**Responsabilidade:** gerenciar a **composição** do sistema, unindo o cliente aos produtos selecionados.

#### Atributos

| Atributo | Visibilidade | Tipo | Descrição |
|---|---|---|---|
| `cliente` | público | `Cliente` | Instância válida da classe `Cliente` |
| `__itens` | privado | `list[Produto]` | Lista de objetos da classe `Produto` |

#### Métodos e propriedades

| Membro | Descrição |
|---|---|
| `adicionar_produto(produto)` | Adiciona uma instância de `Produto` à lista privada `__itens` |
| `remover_produto(produto)` | Remove a instância indicada da lista, se existente |
| `total` (`@property`) | Propriedade calculada: soma dos preços de todos os produtos |
| `listar_itens()` | Exibe na tela todos os produtos usando o formato do `__str__` de `Produto` |

#### Métodos especiais

| Método | Retorno esperado |
|---|---|
| `__str__` | `Carrinho de Maria Silva \| 3 item(ns) \| Total: R$ 374.80` |
| `__repr__` | `CarrinhoDeCompras(cliente=Cliente(...), total_itens=3)` |

---

## Roteiro de homologação (`main.py`)

A execução deve seguir **estritamente** os quatro passos abaixo.

### 1. Instanciação e inspeção de representação

Instanciar ao menos **3 objetos** de `Produto` e **1 objeto** de `Cliente`.
Executar `print(obj)` para validar o `__str__` e `print(repr(obj))` para validar o `__repr__`.

### 2. Validações e captura de exceções (`try/except`)

Comprovar os mecanismos de proteção com atribuições inválidas capturadas por `except ValueError as e:`

- Preço nulo ou negativo — ex.: `p1.preco = -10.0`
- CPF com tamanho incorreto ou caracteres alfabéticos — ex.: `cliente.cpf = "1234"`
- E-mail sem o símbolo `"@"`, ou sem texto antes/depois dele

### 3. Modificadores de visibilidade e *name mangling*

- Demonstrar que o acesso direto a atributos privados (ex.: `p1.__preco`, `cliente.__cpf`)
  gera `AttributeError` fora da classe — o interpretador renomeia o atributo internamente
  para `_Produto__preco` / `_Cliente__cpf`.
- Acessar o atributo protegido (ex.: `p1._categoria`) e **comentar no código** por que o Python
  permite esse acesso, apesar de violar a convenção de boas práticas: o prefixo `_` é apenas
  uma **convenção** entre desenvolvedores ("uso interno"), sem qualquer bloqueio da linguagem.

### 4. Fluxo de carrinho e composição

Instanciar `CarrinhoDeCompras` informando o cliente, adicionar os produtos, invocar
`listar_itens()`, obter o total pela `@property total` e demonstrar a
adição/uso do saldo de cupons do cliente.

---

## Algoritmo de validação de CPF

Parte-se do princípio de que o CPF válido é um texto de **14 caracteres** com a máscara padrão
`999.999.999-99` (ex.: `123.456.789-01`). Fora da máscara ou com dígitos verificadores
inválidos, a validação deve lançar `ValueError`.

### 1ª etapa — Validação do formato (máscara)

Verifica-se se a string coincide com a expressão regular:

```python
r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'
```

Isso garante exatamente 11 dígitos numéricos, com pontos nas posições 3 e 7 e hífen na posição 11.

### 2ª etapa — Verificação de sequências inválidas

CPFs formados por **11 dígitos idênticos** (`000.000.000-00`, `111.111.111-11`, …,
`999.999.999-99`) são considerados inválidos pela Receita Federal, ainda que alguns satisfaçam a
fórmula matemática dos restos. A checagem `len(set(digitos)) == 1` rejeita essas sequências de imediato.

### 3ª etapa — Cálculo do primeiro dígito verificador (DV1)

1. Toma-se os **9 primeiros** dígitos do CPF.
2. Multiplica-se o 1º dígito por 10, o 2º por 9, o 3º por 8, …, e o 9º por 2.
3. Soma-se os produtos: `S1 = (d1×10) + (d2×9) + ... + (d9×2)`.
4. Calcula-se `Resto1 = (S1 * 10) % 11`.
5. Se `Resto1 == 10`, o DV1 esperado é `0`; caso contrário, o DV1 esperado é o próprio `Resto1`.

### 4ª etapa — Cálculo do segundo dígito verificador (DV2)

1. Toma-se os **10 primeiros** dígitos (os 9 originais + o DV1 já verificado/calculado).
2. Multiplica-se o 1º dígito por 11, o 2º por 10, o 3º por 9, …, e o 10º por 2.
3. Soma-se os produtos: `S2 = (d1×11) + (d2×10) + ... + (d10×2)`.
4. Calcula-se `Resto2 = (S2 * 10) % 11`.
5. Se `Resto2 == 10`, o DV2 esperado é `0`; caso contrário, o DV2 esperado é o próprio `Resto2`.
6. Comparam-se os dígitos calculados (DV1 e DV2) com os dois dígitos finais fornecidos na string.

---

## Matriz de avaliação

| Módulo / Item | Requisitos de aceite | Pontuação |
|---|---|---|
| **Módulo Produto** | Atributos das 3 visibilidades, `@property` / `@preco.setter` com `ValueError` se `preco <= 0`, e métodos `__str__` e `__repr__`. | **2,5 pts** |
| **Módulo Cliente** | Atributos de visibilidade variada, validação de e-mail (presença de `@`) e validação completa do CPF, métodos tradicionais de cupom e *dunder methods* `__str__` / `__repr__`. | **2,5 pts** |
| **Módulo Carrinho** | Composição associando cliente e lista privada de produtos, propriedade calculada `total`, método de listagem e dunders `__str__` / `__repr__`. | **2,5 pts** |
| **Script Main & Testes** | Homologação em 4 etapas, tratamento correto de `ValueError` e `AttributeError` em blocos `try/except`, demonstração de composição e clareza de saída. | **2,5 pts** |
| | **Total** | **10,0 pts** |

---

## Entrega

Arquivo único **`.zip`** contendo os módulos `produto.py`, `cliente.py`, `carrinho.py` e o script
principal de homologação `main.py`.

---

## Integrantes

| Integrante | Módulo | Responsabilidade |
|---|---|---|
| *(nome)* | `produto.py` | Classe `Produto` |
| *(nome)* | `cliente.py` | Classe `Cliente` |
| *(nome)* | `carrinho.py` | Classe `CarrinhoDeCompras` |
