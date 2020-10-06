from Criando um Menu.lib.interface import *
from time import sleep

while True:
  resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
  if resposta == 1:
    print('Opção 1')
  elif resposta == 2:
    print('Opção 2)
  elif resposta == 3:
    print('Saindo do sistema... Até logo')
    break 
  else:
    print('\033[31mErro! Digite uma opção valida\033[m')
  sleep(2)
  