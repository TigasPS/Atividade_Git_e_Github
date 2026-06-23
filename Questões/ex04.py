'''
04 - Criar listas com quadrados de 1 a 10.
'''
def criar_listas (x):
    return [i**2 for i in range(1, x+1)]

print (criar_listas(10))