def aumentar(preço = 0, taxa = 0, formato = False):
  res = preço + (preço * taxa/100)
  return res if formato is False else moeda(res)


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
