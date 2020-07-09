casa = float(input('Valor da casa: R$'))
salário = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12)
minimo = salário * 30 / 100
print('Para pagar a casa de R${:.2f} em {} anos'.format(casa, anos), end= '')
print(' a prestação será de R${:.2f}'.format(prestação))
if prestação <= minimo:
    print('Empréstimo pode ser concedido!')
else:
    print('Empréstimo negado')
    