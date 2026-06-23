'''
3 - Considere listas de listas e números. Cada lista, por sua vez, está formada por 
listas e números, recursivamente. Defina uma função achatar que retorne uma lista 
plana com todos os números da lista original. 
Por exemplo, achatar([1, 2, [4, 2], 5, [2, [1, 2, 3], [[1]]], 8]) 
deverá retornar [1, 2, 4, 2, 5, 2, 1, 2, 3, 1, 8]. Dê duas versões, uma sem compreensões 
e outra com compreensões. A versão com compreensões não precisa retornar os elementos na 
ordem em que aparecem os númerosrda à direita de esqueda.
'''
#Sem compreensão:
def acghatar_1 (x):
    lista = []
    if isinstance (x, int):
        return [x]
    else:
        for z in x:
            for y in acghatar_1(z):
                lista.append(y)
        return lista
            
print(acghatar_1([1, 2, [4, 2], 5, [2, [1, 2, 3], [[1]]], 8]))
            
#Com compreensão:

def achatar_2 (x):
    if isinstance(x, int):
        return [x]
    else:
         return [y for z in x for y in achatar_2(z)]

print(achatar_2([1, 2, [4, 2], 5, [2, [1, 2, 3], [[1]]], 8]))
