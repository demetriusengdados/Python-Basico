from Moeda 3 import moeda


p = float(input('Digite o preÃ§o: R$'))
print(f'A metade de {moeda.mode(p)} Ã© {moeda.moeda(moeda.metade(p, True))}')
print(f'O dobro de {moeda.moeda(p)} Ã© {moeda.moeda(moeda.dobro(p, True)}')
print(f'Aumentando 10% temos{moeda.moeda(moeda.aumentar(p, 10, True))}')
print(f'Reduzindo 13%, temos {moedA.diminur(p, 13, True)}')
