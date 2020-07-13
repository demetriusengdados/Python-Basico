distancia = float(input('Qual a distancia da sua viagem? '))
print('Voce esta prestes a comecar uma vigem de {} km'.format(distancia))
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('E o preço da passagem é de R4{:.2f}'.format(preço))
