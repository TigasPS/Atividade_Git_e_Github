'''
07 - Gere uma lista contendo o tamanho de cada palavra.
Ex de entrada: ["python", "java", "javascript", "c"]
'''
def Conta_Letras (x):
    return [len(i) for i in x]

print (Conta_Letras(["python", "java", "javascript", "c"]))
