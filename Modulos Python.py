import Moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {p} é {Moeda.dobro(p)}')
print(f'O dobro de R${p} é R${Moeda.dobro(p)}')
print(f'Aumentando 10% , temos R${Moeda.aumentar(p, 10)}')
