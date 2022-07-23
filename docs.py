def printLines():
    def innerFunc(name):
        print("-"*30)
        func(name)
        print("-"*30)
        return innerFunc

@printLines
def printHello(name):
    print(name)

   # f = printLines()
   # f("rekha")

printHello("rekha")
