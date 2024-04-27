# import xmlrpc.client

# def main():
#     server = xmlrpc.client.ServerProxy('http://localhost:8000')
    
#     while True:
#         n1 = int(input("Enter the first number (or 0 to exit): "))
        
#         if n1 == 0:
#             print("Exiting the program.")
#             break
        
#         n2 = int(input("Enter the second number: "))
#         opp = int(input("Enter 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division (or 0 to exit): "))
        
#         if opp == 0:
#             print("Exiting the program.")
#             break
        
#         result = server.calculate(n1, n2, opp)
#         print(f"Result: {result}")
# if __name__ == '__main__':
#     main()

import xmlrpc.client

def main():
    server = xmlrpc.client.ServerProxy("http://localhost:8000")

    while True:
        n1 = int(input("Enter num1: "))
        if n1==0:
            print("Exiting the program")
            break
        
        n2 = int(input("Enter num2: "))
        opp = int(input("Enter 1 for add, 2 for subtract, 3 for multiply, 4 for divide, (0 for exit: )"))
        if opp==0:
            print("Exitng the program")
            break
        
        result = server.calculate(n1,n2,opp)
        print("Result: ",result)

if __name__=="__main__":
    main()
