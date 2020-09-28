from time import sleep


def contador(i, f, p):
  if p < 0:
    p *= -1
  if p == 0:
    p = 1
  print('-=' * 20)
  print(f'Contagem de {i} até {f} de {p} em {p}')
  sleep(2.5)
  
  if i < f:
    cont = i
    while cont <= f:
      print(f'{cont} ', end='', flush=True)
      sleep(0.5)
      cont += p
    print('Fim')
  else:
    cont = i
    while cont >= f:
      print(f'{cont} ', end='', flush=True)
      sleep(0.5)
      cont -= p
    print('Fim')
    
    
#programa principal
contador(1, 20, 1)
contador(20, 0, 2)
print('-=' * 20)
print('Agora é sua vez')
ini = int(input('Inicio: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)
