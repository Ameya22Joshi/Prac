# import Pyro4
# @Pyro4.expose
# class PalindromeChecker(object):
#     def is_palindrome(self, text):
#         text = text.lower().replace(" ", "")
#         return text == text[::-1]

# daemon=Pyro4.Daemon()
# uri=daemon.register(PalindromeChecker)
# print(uri)
# daemon.requestLoop()

import Pyro4
@Pyro4.expose

class PalindromeChecker(object):
    def ispalindrome(self,text):
        text = text.lower().replace(" ","")
        return text == text[::-1]

daemon = Pyro4.Daemon()
uri = daemon.register(PalindromeChecker)
print(uri)
daemon.requestLoop()