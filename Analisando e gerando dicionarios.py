def notas(*n, sit=False):
  
  """-> Função paraa analisar notas e situações de vários alunos.
  param n: uma ou mais notas de alunos(aceita várias)
  param sit: valor opcional, indicando se deve ou não adicionar a situação
  return: dicionario com várias informações sobre a situação da turma.
  """
  r = dict()
  r['total'] = len(n)
  r['maior'] = max(n)
  r['menor'] = min(n)
  r['média'] = sum(n)/len(n)
  if sit:
    if r['média'] >= 7:
      r['situação'] = 'Boa'
    elif r['média'] >= 5:
        r['situação'] = 'Razoavel'
    else:
          r['situação'] = 'Ruim'
  return r

#executando programa principal
resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
help(notas)
 