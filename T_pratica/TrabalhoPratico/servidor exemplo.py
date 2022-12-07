from math import radians, sin, cos, tan

ângulo = float(input('Escreva o X: '))
seno = sin(radians(ângulo))
print('O seno é:'. format(ângulo, seno))
cosseno = cos(radians(ângulo))
print('O cosseno é:'. format(ângulo, cosseno))
tangente = tan(radians(ângulo))
print('A tangente é:'. format(ângulo, tangente))

