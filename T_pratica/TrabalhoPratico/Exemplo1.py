from math import radians, asin, acos, atan

ângulo = float(input('Escreva o valor de X: '))
ângulo = float(input('Escreva o valor de Y: '))

seno = asin(radians(ângulo))
print('O seno é:'. format(ângulo, seno),seno)
cosseno = acos(radians(ângulo))
print('O cosseno é:'. format(ângulo, cosseno),cosseno)
tangente = atan(radians(ângulo))
print('A tangente é:'. format(ângulo, tangente),tangente)

#from math import radians, acsin, acos, atan

#ângulo = float(input('Escreva o valor de X: '))
#ângulo = float(input('Escreva o valor de Y: '))

#seno = acsin(radians(ângulo))
#print(round(arc_s,2))
#print('O seno é:'. format(ângulo, seno),seno)

#cosseno = degrees(acos(yc))
#print(round(arc_c,2))

#arc_t = degrees(atan(yt))
#$print(round(arc_t,2))