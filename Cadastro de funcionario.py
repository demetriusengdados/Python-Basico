from datetime import datetime
dados = dict()
dados['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['Idade'] = datetime.now().year - nasc
dados['CTPS'] = int(input('Carteira de trabalho(0 não tem): '))
if dados['CTPS'] != 0:
  dados['contratação'] = int(input('Ano de contratação: '))
  dados['Salario'] = float(input('Salário: '))
  dados['Aposentadoria'] = dados['Idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in dados.items():
  print(f'   -{k} tem o valor {v}')
  