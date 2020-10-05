def aumentar(preço = 0, taxa = 0, formato = False):
  res = preço + (preço * taxa/100)
  return res if formato is False else moeda(res)

"""
Função que retorna com ou sem formatação.
param preço: o preço que se quer reajustar
param taxa: qual é a porcentagem de aumento
param formato: quer a saida formatada ou nao.
return: o valor reajustado com ou sem formato
"""

def diminui(preço = 0, taxa = 0, formato = False):
  res = preço - (preço * taxa/100)
  return res if formato is False else moeda(res)


def dobro(preço = 0, formato = False):
  res = preço * 2
  return res if formato is False else moeda(res)


def metade(preço = 0):
  res = preço / 2
  return res 

def moeda(preço = 0, moeda = 'R$'):
  return f'{moeda}{preço}'.replace('.', ',')

def resumo(preço = 0, taxaa = 10, taxar = 5):
  print('-' * 30)
  print('Resumo do valor'.center(30))
  print('-' * 30)
  print(f'Preço Analisado: \t{moeda(preço)}')
  print(f'Dobro do preço: \t{dobro(preço, True)}')
  print(f'Metade do preço: \t{metade(preço, True)}')
  print(f'{taxaa}% de aumento: {aumentar(preço, taxaa, True)}')
  print(f'{taxar}% de redução: {diminui(preço, taxar, True)}')
  print('-' * 30)