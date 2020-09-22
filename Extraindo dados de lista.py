valores = []
while True:
  valores.append(int(input('Digite um valor: ')))
  resp = str(input('Quer continuar? [S/N]'))
  if resp in 'Nn':
    break
print('-=' * 30)
print(f'Voce digitou {len(valores)} elementos')
valores.sort(reverse = True)
print(f'os valores em ordem decrescente são{valores}')
if 15 in valores:
  print('O valor 15 faz parte da lista')
else:
  print('O valor 15 não foi encontrado na lista')
  