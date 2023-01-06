from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
from math import radians, asin, acos, atan


class RequestHandler:
    pass


with SimpleXMLRPCServer(('localhost', 8000),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    server.register_function(pow)
ângulo = float(input('Escreva o valor de X: '))
ângulo = float(input('Escreva o valor de Y: '))

seno = asin(radians(ângulo))
print('O seno é:'. format(ângulo, seno),seno)
cosseno = acos(radians(ângulo))
print('O cosseno é:'. format(ângulo, cosseno),cosseno)
tangente = atan(radians(ângulo))
print('A tangente é:'. format(ângulo, tangente),tangente)