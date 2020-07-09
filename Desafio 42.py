r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 <r1 + r3 and r3 < r1 + r2:
    print('Os triangulos acima podem formar um teiangulo ', end='')
    if r1 == r2 == r3:
        print('Equilatero')
    elif r1 != r2 != r3 != r1:
        print('Escaleno')
    else:
        print('Isoceles')
else:
        print('Os segmentos acima não podem formar um triangulo')
        
        