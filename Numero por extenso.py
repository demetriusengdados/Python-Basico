cont = ('zero', 'um', 'dois', 'tres', 'quatro'
        'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'quatorze'
        'quinze', 'dezesseis', 'dezesete', 'dezoito'
        'dezenove', 'vinte')
while True:
    num = int(input('Digite um numero entre 0 e 20'))
    if 0 <= num <= 20:
        break
    print('tente Novamente. ', end='')
print(f'Voce digitou o numero {cont[]}')

