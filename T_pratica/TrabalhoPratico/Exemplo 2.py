from math import radians

#import numpy
from numpy import arcsin
from numpy import arccos
from numpy import arctg

#numpy.arcsin

ângulo = float(input('Escreva o valor de X: '))
ângulo = float(input('Escreva o valor de Y: '))

seno = arcsin(radians(ângulo))
print('O seno é:'. format(ângulo, seno),seno)
cosseno = arccos(radians(ângulo))
print('O cosseno é:'. format(ângulo, cosseno),cosseno)
tangente = arctg(radians(ângulo))
print('A tangente é:'. format(ângulo, tangente),tangente)