print('{:=^40}'.format('Lojas da Mata'))
preço = float(input('preço das compras: R$'))
print('''Formas de pagamento
      [1] á vista dinheiro/cheque
      [2] á vista cartão
      [3] 2x no cartão
      [4] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas Parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totparc, parcela))
else:
    total = 0
    print('Opção Invalida. Tente novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preço, total))
       
              