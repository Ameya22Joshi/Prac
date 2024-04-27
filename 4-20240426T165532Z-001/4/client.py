# import Pyro4

# def main():
#     uri = input("enter server uri: ")
#     checker = Pyro4.Proxy(uri)
#     text = input("Enter a string to check if it's a palindrome: ")
#     is_palindrome = checker.is_palindrome(text)
    
#     if is_palindrome:
#         print(f"'{text}' is a palindrome.")
#     else:
#         print(f"'{text}' is not a palindrome.")
# if __name__ == "__main__":
#     main()

import Pyro4

def main():
    uri = input("Enter uri of server: ")
    checker = Pyro4.Proxy(uri)
    str = input("Enter a String: ")
    is_palindrome = checker.ispalindrome(str)

    if(is_palindrome):
        print(str," is palinddrome")
    else:
        print(str, " is not palindrome")

if __name__ == "__main__":
    main()