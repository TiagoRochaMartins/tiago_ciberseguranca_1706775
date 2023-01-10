# tiago_ciberseguranca_1706775
<p >Nome: Tiago Rocha Martins  Nº1706775</p>
<p >Curso: Ciberseguranca</p>
<p >Disciplina: Sistemas Distribuídos</p>

![alt text](./imagens/IPG.png)

# Relatório do Trabalho Prático
# Sistemas Distribuídos

## Nome do Trabalho: Função trigonométrica inversa



## Aluno: Tiago Martins, Número:1706775,
## Github:https://github.com/TiagoRochaMartins, 
## Email:tiagorochamartins19@gmail.com
## No GITHUB o código do servidor e do client encontram-se na pasta T_pratica/TrabalhoPratico

## 1.Descrição do Trabalho
Este trabalho consiste na criação de uma função no servidor: implementar função inv_trignometria(x,y) que calcula os valores da função arccos, arcsin ,arctg 
indicada em x com argumento y (exemplo arccos(y)) e retorna ao cliente o resultado. 
cliente envia a função a calcular e o argumento para o servidor retornar o seu valor. 

## 2.Função implementada	
  //Esta é a função que foi implementada no servidor
  <p >def inv_trignometria(x,y):</p>
    <p >return x + y</p> 

## 3.Servidor	

<p >from xmlrpc.server import SimpleXMLRPCServer</p>
<p >from xmlrpc.server import SimpleXMLRPCRequestHandler</p>

//Nas duas linhas em baixo vamos restringir a um caminho específico
<p >class RequestHandler(SimpleXMLRPCRequestHandler):</p>
    <p >rpc_paths = ('/RPC2',)</p>

//Nas duas linhas de baixo vamos definir a função
<p >def inv_trignometria(x,y):</p>
   <p >return x + y</p>    

//Nas três linhas em baixo vamos criar o servidor
<p >with SimpleXMLRPCServer(('localhost', 8000),</p>
                       <p >requestHandler=RequestHandler) as server:</p>
    <p >server.register_introspection_functions()</p>

//A última linha vai executar o loop principal do servidor
    <p >server.serve_forever()</p>

## 4.Client	

<p >import xmlrpc.client</p>

<p >s = xmlrpc.client.ServerProxy('http://localhost:8000')</p>

//Na linha de baixo a partir do módulo math vamos importar várias funções.
<p >from math import radians, asin, acos, atan</p>

//Nas duas linhas abaixo vamos ler o X e o Y.
<p >ângulo = float(input('Escreva o valor de X: '))</p>
<p >ângulo = float(input('Escreva o valor de Y: '))</p>

// Na linha em baixo o ângulo que eu escrevi vai ser convertido para radianos e calcular o asin
<p >seno = asin(radians(ângulo))</p>
// Na linha em baixo vai ser o output
<p >print('O asin é:'. format(ângulo, seno),seno)</p>
// Na linha em baixo o ângulo que eu escrevi vai ser convertido para radianos e calcular o acos
<p >cosseno = acos(radians(ângulo))</p>
// Na linha em baixo vai ser o output
<p >print('O acos é:'. format(ângulo, cosseno),cosseno)</p>
// Na linha em baixo o ângulo que eu escrevi vai ser convertido para radianos e calcular a atan
<p >tangente = atan(radians(ângulo))</p>
// Na linha em baixo vai ser o output
<p >print('A atan é:'. format(ângulo, tangente),tangente)</p>

<p >print(s.system.listMethods())</p>

## 5.Funcionamento do trabalho	
Como é possível ver na imagem em baixo podemos ver o client e o servidor a funcionarem
![alt text](./Afuncionar.PNG)
## 6.Conclusão
<p >Neste trabalho o que foi feito foi criar um cliente e um servidor.</p>
<p >No cliente criei um módulo chamado math e criei as funções radians, asin, acos, atan.
Criei duas linhas em que vai ser pedido o valor de X e de Y.
Nas linhas de baixo basicamente o ângulo vai ser convertido para radianos e calcular o asin, acos e atan.
E na outra linha vai sair o respetivo output do cálculo.</p>
<p >No servidor resumidamente defini uma função e criei um servidor.</p>
<p >Resumidamente o cliente vai enviar uma função a calcular e o argumento para o servidor retornar o seu valor.</p>





branch auxiliar


