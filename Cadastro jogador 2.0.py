time = list()
jogador = dict()
partidas = list()

while True:
  jogador.clear()
  jogador['nome'] = str(input('Nome do jogador: '))
  tot = int(input('Quantas partidas {jogador["nome"]} jogou? '))
  partidas.clear()
  for c in range(0, tot):
    partidas.append(int(input(f' Quantos gols na partida {c+1}? ')))
  jogador['gols'] = partidas[:]
  jogador['totl'] = sum(partidas)
  time.append(jogador.copy())
  while True:
    resp = str(input('Quer continuar? [S/N]')).upper()[0]
    if resp in 'SN':
      break
    print('Erro! Responda S ou N')
  if resp == 'N':
    break
print('-=' * 30)
print('cod', end='')
for i in jogador.keys():
  print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
  print(f'{k:>3} ', end='')
  for d in v.values():
    print(f'{str(d):<15}', end='')
  print()
print('-' * 40)
while True:
  busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
  if busca == 999:
    break
  if busca >= len(time):
    print(f'Erro! Não existe jogador com codigo {busca}')
  else:
    print(f' --Levantamento do jogador{time[busca] ["nome"]}: ')
    for i, g in enumerate(time[busca]['gols']):
      print(f'  No jogo {i+1} fez {g} gols')
  print('-' * 40)
print('<< Volte Sempre >>')
`