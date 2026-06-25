'''
02 - Defina a função "descendentes" que pega uma árvore genealógica e retorna 
todos os descendentes da raiz. Utilize compreensões.
'''

def descendentes(arvore):
    nome, filhos = arvore
    return [filho[0] for filho in filhos] + [d for filho in filhos for d in descendentes(filho)]


arvore = ("João", [
    ("Maria", [
        ("Ana", []),
        ("Pedro", [])
    ]),
    ("Carlos", [])
])

print(descendentes(arvore))

    