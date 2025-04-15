from random import shuffle
n1 = str(input('Nome do aluno 1: '))
n2 = str(input('Nome do aluno 2: '))
n3 = str(input('Nome do aluno 3: '))
n4 = str(input('Nome do aluno 4: '))
alunos = [n1, n2, n3, n4]
shuffle(alunos)
print('A ordem de apresentação será: {}'.format(alunos))
