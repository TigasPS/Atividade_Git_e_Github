'''
05 - Dada uma lista com nomes, filtrar palavras maiores que 5 letras.
'''
def Maior_que_5 (x):
    return [i for i in x if len(i)>5]

print (Maior_que_5(['Brasil','Hexa','Neymar','Endrick','Tiago','Santos','Pinheiro']))