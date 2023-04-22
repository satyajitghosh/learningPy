## Anpther phenomenon - 
## While the email and fullname are defined as funcions in the class Employee,
## decorating them with @property helps us access these functions
## as data members of the class
## email and full name can also be assigned values just like other data members

class Employee:
    def __init__(self,first,last) -> None:
        self.first = first
        self.last = last
    @property
    def email(self):
        return f"{self.first}.{self.last}@email.com"
    @property
    def fullname(self):
        return f"{self.first} {self.last}"
    
    @fullname.setter
    def fullname(self,full_name):
        first,last = full_name.split()
        self.first = first
        self.last = last
    

def main():
    emp = Employee('Satyajit','Ghosh')
    print(emp.fullname)
    print(emp.email)
    # When we change the surname, the email and fullname are automatically changed.
    emp.last = 'Ray'
    print(emp.fullname)
    print(emp.email)

    # As we have define fullname.setter, this will allow us to set the fullname data member.
    # Well, not exactly the fullname data member, because inside the class it codes not exist.
    # But, it will allow us to set the underlying variables - first and last, which are recognized
    # inside the class.
    # Re-setting the fullname to 'Satyajit Ghosh'

    emp.fullname = 'Satyajit Ghosh'
    print(emp.fullname)
    print(emp.email)

    ## Note - as we have note defined an email.setter methodinside the class,
    ## we will not be able to assign value to emp.email in a similar way.
    ## ie. the following will fail.
    ## emp.email = 'Satyajit.Ghosh@email.com'
    ## unless we define a setter function with property @email.setter




if __name__ == '__main__':
    main()
