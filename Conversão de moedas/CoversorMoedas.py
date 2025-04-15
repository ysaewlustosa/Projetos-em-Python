print('Conversor de moedas')
valor = float(input('Digite o valor em reais: '))

dolar = valor / 5.04
euro = valor / 6.13
libra = valor / 7.13

print(f'O valor em dólar é: {dolar:.2f}')
print(f'O valor em euro é: {euro:.2f}')
print(f'O valor em libra é: {libra:.2f}')
