numeros = list()
while True:
  n = int(input('Digite um valor: '))
  if n not in numeros:
    numeros.append(n)
    print('valor adicionado com sucesso...')
  else:
    print('Valor duplicado, não vou adicionar...')
  r = str(input('Quer continuar? [S/N]'))
  if r in 'Nn':
    break
print('-=' * 30)
numeros.sort()
print(f'Voce digitou os valores {numeros}')
