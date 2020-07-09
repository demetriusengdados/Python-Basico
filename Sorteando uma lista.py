from random import choice 
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro Aluno: '))
n4 = str(input('Quarto aluno: '))
n5 = str(input('Quinto aluno: '))
lista = [n1, n2, n3, n4, n5]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
