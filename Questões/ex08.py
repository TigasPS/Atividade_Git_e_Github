'''
08 - Faça uma lista com os números pares de uma lista de inteiros.
'''
def Numeros_Pares (x):
    return [i for i in x if i%2 == 0]

print (Numeros_Pares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))