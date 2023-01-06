
from math import radians, asin, acos, atan

ângulo = float(input('Escreva o valor de X: '))
ângulo = float(input('Escreva o valor de Y: '))

seno = asin(radians(ângulo))
print('O seno é:'. format(ângulo, seno),seno)
cosseno = acos(radians(ângulo))
print('O cosseno é:'. format(ângulo, cosseno),cosseno)
tangente = atan(radians(ângulo))
print('A tangente é:'. format(ângulo, tangente),tangente)
