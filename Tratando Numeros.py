num = cont = soma = 0
num = int(input('Digite um numero [999 para para]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um numero [999 para para]: '))
print('Voce digitou {} numeros e a soma entre eles foi {}'.format(cont, soma))
