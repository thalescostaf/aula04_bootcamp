from typing import Dict, Any

# Exemplo de lista
lista_01: list = ['Thales', 'Lais']
print(lista_01)

# Exemplo de dicionário
produto_01: list = {
    'nome': 'Thales',
    'idade': 30
}

produto_02: list = {
    'nome': 'Lais',
    'idade': 31
}

print(produto_01, produto_02)


livro: Dict[str, Any] = {
    'Título': 'Game of Thrones',
    'Autor': 'Estagiario',
    'Ano': 2005
}

print(livro)

# Como imprimir todos os itens do dicionário
lista_elementos: list = livro.items()
for elemento in lista_elementos:
    print(elemento)
