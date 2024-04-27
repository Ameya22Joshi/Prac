# import Pyro4
# @Pyro4.expose
# class stringconcatenator:
#     def concatenate(self,str1,str2):
#         return str1+str2

# daemon=Pyro4.Daemon()
# uri=daemon.register(stringconcatenator)
# print(uri)
# daemon.requestLoop()

import Pyro4
@Pyro4.expose

class stringconcatenator:
    def concatenate(self,str1,str2):
        return str1 + str2

daemon = Pyro4.Daemon()
uri = daemon.register(stringconcatenator)
print(uri)
daemon.requestLoop()