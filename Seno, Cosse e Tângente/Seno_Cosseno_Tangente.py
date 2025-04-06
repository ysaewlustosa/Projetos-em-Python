#Ex 18
from math import sin, cos, tan, radians
angulo = float(input("Digite o ângulo em graus: "))
print(f'O ângulo de {angulo} tem o SENO de {sin(radians(angulo)):.2f}')
print(f'O ângulo de {angulo} tem o COSSENO de {cos(radians(angulo)):.2f}')
print(f'O ângulo de {angulo} tem a TANGENTE de {tan(radians(angulo)):.2f}')
