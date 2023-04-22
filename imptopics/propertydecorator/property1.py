# Why is all of this required?
# To make the data member private, there is no direct way in python to do so.
# Which is why we do it through getter and setter.
# Unless we define the setter method we will not be able to runthe command - fruit.name = 'Orange'
# While assigning through the setter method we can also deploy additional checks.
# Such as assert that the name of the fruit should be string and atleast 3 characters in length.
# Or, a variable like age should be greater than zero.


class Fruit:
    def __init__(self,name):
        self._name = name
    @property
    def name(self) -> str:
        print(f"{self._name} was accessed.")
        return self._name
    @name.setter
    def name(self,name) -> None:
        print(f"{self._name} is now {name}.")
        self._name = name
    @name.deleter
    def name(self) -> None:
        print(f"{self._name} was deleted.")
        self._name = None

def main():
    fruit = Fruit('Apple')
    print(fruit.name)
    fruit.name = 'Orange'
    print(fruit.name)
    del fruit.name
    print(fruit.name)
    

if __name__ == '__main__':
    main()
