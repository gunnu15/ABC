class myClass:
    __privateVar = 27;
    def __privMeth(self):
        print("I am inside class, myClass")
    def hello(self):
        print("Private Variable value:", self.__privateVar)
foo = myClass()
foo.hello()
foo.__privMeth()