'''
09 - Crie uma lista com todos os números primos de 1 a n.
'''
def primo(n):
    return len([c for c in range(1, n + 1) if n % c == 0]) == 2
def lista(n):

    return [x for x in range(1, n + 1) if primo(x)]

print(lista(int(input())))