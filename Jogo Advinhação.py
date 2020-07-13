from random import randint
from time import sleep
computador = randint(0, 5) #faz o computador "PENSAR"
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que numero pensei? ')) # jogador tenta adivinhar
print('Processando...')
sleep(3)
if jogador == computador:
    print('Parabens voce me venceu')
else:
    print('Ganhei! Eu pensei no numero {} e não no {}'.format(computador, jogador))
