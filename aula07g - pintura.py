# essa não sei
largura = float(input('Largura da parede? '))
altura = float(input('Altura da parede '))
area = largura * altura
print('Sua parede tem a dimensão de {} x {} e sua área é de {}m2'.format(largura, altura, area))
print('Para pintar essa parede você vai precisar de {}l de tinta.'.format(area/2))