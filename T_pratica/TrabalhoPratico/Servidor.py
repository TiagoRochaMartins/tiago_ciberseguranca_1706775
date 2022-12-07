from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
with SimpleXMLRPCServer(('localhost', 8000),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    server.register_function(pow)

    def inv_trignometria(x, y):
        return x + y
    server.register_function(inv_trignometria, 'inv_trignometria')

    class MyFuncs:


    server.register_instance(MyFuncs())

    server.serve_forever()