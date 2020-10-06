from Criando Menu.lib.interface import *


def arquivoExiste(nome):
  try:
    a = open(nome, 'rt')
    a.close()
  except FileNotFoundError:
    return False
  else:
    return True
  
  
def criarArquivo(nome):
  try:
    a = open(nome, 'wt+')
    a.close()
  except:
    print('Houve um erro ao criar o arquivo')
  else:
    print(f'Arquivo {nome} criado com sucesso')
    
    
def lerArquivo(nome):
  try:
    a = open(nome, 'rt')
  except:
    print('Erro ao ler arquivo')
  else:
    cabeçalho('Pessoas cadastradas)
    print(a.read())
    