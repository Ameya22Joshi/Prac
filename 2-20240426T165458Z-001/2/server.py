# from xmlrpc.server import SimpleXMLRPCServer

# def arithmetic(n1,n2,opp):
#     if opp==1:
#         return n1+n2
#     elif opp==2:
#         return n1-n2
#     elif opp==3:
#         return n1*n2
#     elif opp==4:
#         return n1/n2
#     else:
#         return("not an operator")
        
# server=SimpleXMLRPCServer(('localhost',8000))
# server.register_function(arithmetic,'calculate')
# server.serve_forever()

from xmlrpc.server import SimpleXMLRPCServer

def arithmetic(n1,n2,opp):
    if opp==1:
        return n1+n2
    elif opp==2:
        return n1-n2
    elif opp==3:
        return n1*n2
    elif opp==4:
        return n1/n2
    else:
        return("not an operator")

server = SimpleXMLRPCServer(('localhost',8000))
server.register_function(arithmetic,"calculate")
server.serve_forever()