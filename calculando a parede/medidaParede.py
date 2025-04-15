largura=float(input('Largura da parede: '))
comprimento=float(input('Comprimento da parede: '))

lataTinta = 2


area = largura * comprimento
litros = area / lataTinta

print(f'Área da parede: {area} m²')
print(f'Litros de tinta necessários: {litros} L')
print(f'Quantidade de latas de tinta necessárias: {litros / 18}')

