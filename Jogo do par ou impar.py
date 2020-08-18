from random import randint
v = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 20)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print(f'Voce jogou {jogador} e o computador {computador}. Total de {total} ', end='' )
    print('Deu PAR' if total % 2 == 0 else 'Deu IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Voce Venceu!')
            v += 1
        else:
            print('Voce Perdeu')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Voce venceu')
            v += 1
        else:
            print('Voce perdeu')
            break
    print('Vamos jogar novamente')
print(f'GAME OVER! Voce venceu {v} vezes')
