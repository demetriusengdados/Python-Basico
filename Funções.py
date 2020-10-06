def leiaInt(msg):
  while True:
    try:
      n = int(input(msg))
    except (ValueError, TypeError):
      print('\033[31mErro: por favor digite um numero valido.\033[m')
      continue
    except (KeyboardInterrupt):
      print('\n\033[31mUsuário preferiu não digitar esse numero\033[m')
      return 0
    else:
      return n
    
    
def leiaFloat(msg):
  while True:
    try:
      n = int(input(msg))
    except (ValueError, TypeError):
      print('\033[31mErro: por favor digite um numero valido.\033[m')
      continue
    except (KeyboardInterrupt):
      print('\n\033[31mUsuário preferiu não digitar esse numero\033[m')
      return 0
    else:
      return n
    
num = leiaInt('Digite um valor: ')
print(f'O valor digitdo foi {num}')
