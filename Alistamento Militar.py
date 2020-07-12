from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você deve se alistar!')
elif idade < 18:
    saldo = 18 - idade
    print('Você ainda não deve se alistar, faltam {} anos para o alistamento.')
    ano = atual + saldo
    print('Seu alistamento sera em {}')
elif idade > 18:
   saldo = idade - 18
   print('Voce ja deveria ter se alistado ha {} anos'.format(saldo))
   ano = atual - saldo
   print('Seu alistamento foi em {}'.format(ano))


   
