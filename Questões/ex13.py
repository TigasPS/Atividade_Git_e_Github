'''
13 - Dada uma matriz de inteiros, me faça uma lista com apenas os numeros pares da matriz.
'''
def pares_da_matriz (m):
    return [i for n in m for i in n if i%2==0]

print(pares_da_matriz([[1,2,3,4],[5,6,7,8]]))