'''
11 - Dada uma lista com as notas de todos os alunos de uma turma, 
retorne a quantidade de alunos acima da média, que é 5.
'''

def Acima_da_média (x):
    return sum([1 for i in x if i > 5])

print(Acima_da_média([10,4,20,3,3,4,8,9,2,34]))