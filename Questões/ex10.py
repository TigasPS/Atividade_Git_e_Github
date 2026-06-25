'''
10 - Dada uma lista numérica, retorne apenas os números positivos
'''

def nums_positivos (x):
    return [i for i in x if i > 0]

print(nums_positivos([-3, -2, -1, 0, 1, 2, 3]))