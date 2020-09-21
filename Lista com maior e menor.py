listanum = []
mai = 0
men = 0
for c in range(0, 10):
  listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
  if c == 0:
    mai = men = listanum[c]
  else:
    if listanum[c] > mai:
      mais = listanum[c]
    if listanum[c] < men:
      men = listanum[c]
print('=-' * 30)
print(f'Voce digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai} nas posções', end='')
for i, v in enumerate(listanum):
  if v == mai:
    print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {men} nas posições', end='')

for i, v in enumerate(listanum):
  if v == men:
    print(f'{i}...', end='')
print()
