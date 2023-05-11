from abc import ABC,abstractmethod

class IA(ABC):
    @abstractmethod
    def methodA(self):
        pass

class A:
    def methodA(self):
        print('method A')

class IB(ABC):
    @abstractmethod
    def methodB(self):
        pass
class B:
    def methodB(self):
        print('method B')


# Now, there isn't a way for class a to call method b. It can only call method a.
# That is why we create another adapter class.

class BAdapter(IA):
    def __init__(self):
        self.classb = B()
    def methodA(self):
        self.classb.methodB()         

item = BAdapter()
item.methodA()

# Another way
# Here, the object of a class of type IB is passed to the adapter during instatntiattion.
# This gives us the the indepedence to pass any class of type IB to the adapter.
#  
class BAdapter2(IA):
    def __init__(self,typebclass:IB):
        self.classb = typebclass
    def methodA(self):
        self.classb.methodB()

item = BAdapter2(B())
item.methodA()