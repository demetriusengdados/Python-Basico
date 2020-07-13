from random import shuffle 
n1 = str(input('Primeiro aluno; '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
n5 = str(input('Quinto aluno: '))
n6 = str(input('Sexto aluno: '))
lista = [n1, n2, n3, n4, n5, n6]
shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)
