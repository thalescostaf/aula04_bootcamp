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



livro_01: Dict[str, Any] = {
    'Título': 'Game of Thrones',
    'Autor': 'Estagiario',
    'Ano': 2005
}

livro_02: Dict[str, Any] = {
    'Título': 'A saga do Estagiario',
    'Autor': 'Luciano',
    'Ano': 2004
}


# Como imprimir todos os itens do dicionário
lista_elementos: list = livro.items()
for elemento in lista_elementos:
    print(elemento)


lista_de_livros = []
lista_de_livros.append(livro_01)
lista_de_livros.append(livro_02)

print(lista_de_livros)
