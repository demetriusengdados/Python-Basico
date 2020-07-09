from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('Classificação: Mirim')
elif idade <= 14:
    print('Classifição: Infantil')
elif idade <= 19:
    print('Classificação: Junior')
else:
    print('Classificação: Master')
    
    