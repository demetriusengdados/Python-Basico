from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesour''')
jogador = int(input('Qual é sua jogada?'))
print('-=' * 11)
print('O computador escolheu {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0:
    if jogador == 0:
print('Empate')
elif jogador == 1:
print('Jogador vence')
elif jogador == 2:
print('Computador Vence')
else:
     print('Jogada Invalida')

elif computador == 1:
if jogador == 0:
print('Empate')
elif jogador == 1:
print('Jogador vence')
elif jogador == 2:
print('Computador Vence')
else:
     print('Jogada Invalida')
 
elif computador == 2:
if jogador == 0:
print('Empate')
elif jogador == 1:
print('Jogador vence')
elif jogador == 2:
print('Computador Vence')
else:
     print('Jogada Invalida')
     