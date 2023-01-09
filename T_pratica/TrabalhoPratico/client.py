import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:8000')

from math import radians, asin, acos, atan

ângulo = float(input('Escreva o valor de X: '))
ângulo = float(input('Escreva o valor de Y: '))

seno = asin(radians(ângulo))
print('O asin é:'. format(ângulo, seno),seno)
cosseno = acos(radians(ângulo))
print('O acos é:'. format(ângulo, cosseno),cosseno)
tangente = atan(radians(ângulo))
print('A atan é:'. format(ângulo, tangente),tangente)

print(s.system.listMethods())


