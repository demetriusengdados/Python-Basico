times = ('Corinthians', 'Palmeiras', 'Santos', 'Gremio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia',
         'São Paulo', 'Fluminense', 'Sport Reciffe', 
         'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 
         'Atlético-GO')
print('-=' * 15)
print(f'Lista de time do Brasileirão: {times}')
print('-=' * 15)
print(f'Os 5 Primeiros sãao {times[0:5]}')
print('-=' * 15)
print('Os 4 Ultimos são {times[-4:]}')
print('-=' * 15)
print(f'TImes em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'O Chapecoense está na posição {times.index("Chapecoense")+1}posição')
