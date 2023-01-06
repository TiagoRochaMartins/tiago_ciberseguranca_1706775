# tiago_ciberseguranca_1706775
nome: TiagoMartins1706775
curso: Ciberseguranca 
Disciplina: Sistemas Distribuídos

![alt text](./imagens/IPG.png)

# Relatório do Trabalho prático
# Sistemas Distribuídos

## Função trigonométrica inversa



## Aluno: Tiago Martins, Número:1706775,
## Github:https://github.com/TiagoRochaMartins, 
## Email:tiagorochamartins19@gmail.com

## 1.Descrição do Trabalho
Este trabalho consiste na criação de uma função no servidor: implementar função inv_trignometria(x,y) que calcula os valores da função arccos, arcsin ,arctg 
indicada em x com argumento y (exemplo arccos(y)) e retorna ao cliente o resultado. 
cliente envia a função a calcular e o argumento para o servidor retornar o seu valor. 

## 2.Função implementada	
  // colocar a descrição da função a implementar no servidor e explica-la 

## 3.Servidor	

from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

//Nas duas linhas em baixo vamos restringir a um caminho específico
class RequestHandler(SimpleXMLRPCRequestHandler): 
    rpc_paths = ('/RPC2',)

//Nas três linhas em baixo vamos criar o servidor
#with SimpleXMLRPCServer(('localhost', 8000), 
                       #requestHandler=RequestHandler) as server:
    #server.register_introspection_functions()

//A última linha vai executar o loop principal do servidor
    #server.serve_forever()

## 4.Client	

#import xmlrpc.client

#s = xmlrpc.client.ServerProxy('http://localhost:8000')

//Na linha em baixo a partir do módulo math vamos importar várias funções.
#from math import radians, asin, acos, atan

//Nas duas linhas em baixo vamos ler o X e o Y.
#ângulo = float(input('Escreva o valor de X: '))
#ângulo = float(input('Escreva o valor de Y: '))

// Na linha em baixo o ângulo que eu escrevi vai ser convertido para radianos e calcular o asin
#seno = asin(radians(ângulo))
// Na linha em baixo vai ser o output
#print('O asin é:'. format(ângulo, seno),seno)
// Na linha em baixo o ângulo que eu escrevi vai ser convertido para radianos e calcular o acos
#cosseno = acos(radians(ângulo))
// Na linha em baixo vai ser o output
#print('O acos é:'. format(ângulo, cosseno),cosseno)
// Na linha em baixo o ângulo que eu escrevi vai ser convertido para radianos e calcular a atan
#tangente = atan(radians(ângulo))
// Na linha em baixo vai ser o output
#print('A atan é:'. format(ângulo, tangente),tangente)

#print(s.system.listMethods())

## 5.Funcionamento do trabalho	
Como é possível ver na imagem em baixo podemos ver o client e o servidor a funcionarem
![alt text](./Afuncionar.PNG)
## 6.Conclusão
// descrever brevemente o que se fez e o que faltou fazer

## Bibliografia



branch auxiliar


