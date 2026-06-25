'''
12 - Crie uma lista que que extraia todas as letras das palavras 
e gere uma única lista. Ex: palavras = ["python", "java"]. 
Saída = ['p', 'y', 't', 'h', 'o', 'n', 'j', 'a', 'v', 'a']
'''
def separador (x):
    return [y for i in x for y in i]

print(separador(["python", "java"]))