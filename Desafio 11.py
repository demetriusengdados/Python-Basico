larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = alt * larg
print('Sua parede a dimensão de {}x{} e sua área é de {}m2.'.format(larg, alt, area))
tinta = area / 2
print('Para pintar essa parede, voce precisara de {}L de tinta.'.format(tinta))

