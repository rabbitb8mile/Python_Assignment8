class A:
    
        a=None
        _b=None#_ represents proptected
        __c=None#__ represents private
        def __init__(self,a,b,c):
            self.a=a
            self._b=b
            self.__c=c
        def display1(self):
             print("This is class A")
             print(self.a)
             print(self._b)
             print(self.__c)

class B(A):
    def display2(self):
        print("this is class B")
        try:
            print("class B")
            print("c:",self.__c)
        except AttributeError:
            print("cannot access private members ")
            print("a:",self.a)
            print("b:",self._b)
        print()

        

b=B(1,2,3)
b.display2()



