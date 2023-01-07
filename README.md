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
<br />class RequestHandler(SimpleXMLRPCRequestHandler):<br />
    <br />rpc_paths = ('/RPC2',)<br />

//Nas três linhas em baixo vamos criar o servidor
<br />with SimpleXMLRPCServer(('localhost', 8000),<br />
                       <br />requestHandler=RequestHandler) as server:<br />
    <br />server.register_introspection_functions()<br />

//A última linha vai executar o loop principal do servidor
    <br />server.serve_forever()<br />

## 4.Client	

<br />import xmlrpc.client<br />

<br />s = xmlrpc.client.ServerProxy('http://localhost:8000')<br />

//Na linha em baixo a partir do módulo math vamos importar várias funções.
<br />from math import radians, asin, acos, atan<br />

//Nas duas linhas em baixo vamos ler o X e o Y.
<br />ângulo = float(input('Escreva o valor de X: '))<br />
<br />ângulo = float(input('Escreva o valor de Y: '))<br />

// Na linha em baixo o ângulo que eu escrevi vai ser convertido para radianos e calcular o asin
<br />seno = asin(radians(ângulo))<br />
// Na linha em baixo vai ser o output
<br />print('O asin é:'. format(ângulo, seno),seno)<br />
// Na linha em baixo o ângulo que eu escrevi vai ser convertido para radianos e calcular o acos
<br />cosseno = acos(radians(ângulo))<br />
// Na linha em baixo vai ser o output
<br />print('O acos é:'. format(ângulo, cosseno),cosseno)<br />
// Na linha em baixo o ângulo que eu escrevi vai ser convertido para radianos e calcular a atan
<br />tangente = atan(radians(ângulo))<br />
// Na linha em baixo vai ser o output
<br />print('A atan é:'. format(ângulo, tangente),tangente)<br />

<br />print(s.system.listMethods())<br />

## 5.Funcionamento do trabalho	
Como é possível ver na imagem em baixo podemos ver o client e o servidor a funcionarem
![alt text](./Afuncionar.PNG)
## 6.Conclusão
// descrever brevemente o que se fez e o que faltou fazer

## Bibliografia



branch auxiliar


