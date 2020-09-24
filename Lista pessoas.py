#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pessoa = dict()
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F]')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro! Por favor digite apenas M ou F')
        pessoa['idade'] = int(input('Idade: '))
        soma += pessoa ['idade']
        galera.append(pessoa.copy())
        while True:
            resp = str(input('Quer continuar? [S/N]')).upper()[0]
            if resp in 'SN':
                break
print('-=' * 60)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
média = soma / len(galera)
print(f'B) A média de idade é de {média:5.2f} anos')
print(f'C) as mulheres cadastradas foram', end ='')
print()
print(f'D) Lista de pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= média:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}', end='')
        print()
print('<< Encerrado >>')


# In[ ]:




