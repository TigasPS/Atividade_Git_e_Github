'''
06 - Contar quantidade de vogais em uma string.
'''
def Conta_vogais (x):
    return sum([1 for i in x if i in 'aeiouAEIOU'])
x = input()
print (Conta_vogais(x))