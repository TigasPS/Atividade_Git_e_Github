'''
01 - Defina uma função que leia do teclado uma sequência de números inteiros dados 
em uma única linha. A função deve retornar uma lista contendo os números que 
estão na linha.
'''

def ler_numeros ():
    lista = [int(x) for x in input().split()]
    return lista
resultado = ler_numeros()
print (resultado)