print('Este programa lê a largura e altura de uma parede\ne mostra a quantidade de tinta '
      'necessário para pintar essa parede')
largura = float(input('Informe a largura da janela: '))
altura = float(input('Informe a altura da janela: '))
area = largura*altura
tinta = area/2
print('Largura da parede: {}m\nAltura da parede: {}m\nArea da parede: {}m²\nQuantidade de litros de tinta necessário para pintar a parede: {}L'.format(largura, altura, area, tinta))
