# import xmlrpc.client

# def main():
#     server=xmlrpc.client.ServerProxy('http://localhost:8000')
#     n=int(input("enter the number"))
#     result=server.calculate_factorial(n)
#     print(result)
# if __name__=='__main__':
#     main()

import xmlrpc.client

def main():
    server = xmlrpc.client.ServerProxy('http://localhost:8000')
    n = int(input("Enter a number: "))
    result = server.calculate_factorial(n)
    print(result)

if __name__ =='__main__':
    main()
