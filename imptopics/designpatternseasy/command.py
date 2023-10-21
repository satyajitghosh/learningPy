'''The execution/invocation of the command is completely separated from the
steps of the command.Therefore the client code written in main just needs 
to know that the object it has been passed will have an execute command
and it will execute the same.'''

'''What needs to be called inside the taskset is specified within ComplexCommand'''
'''Provides the client code the ability to execute commands seemlessly.'''

'''Another example - https://refactoring.guru/design-patterns/command'''

from abc import ABC,abstractmethod
class Command:
    @abstractmethod
    def execute():
        pass

class SimplePrintCommand(Command):
    def __init__(self,s:str) -> None:
        self.s = s
    def execute(self):
        print(self.s)

class Taskset:
    def do_something_1(self):
        print('Doing Task 1')
    def do_something_2(self):
        print('Doing Task 2')

class ComplexCommand(Command):
    def __init__(self,task:Taskset) -> None:
        self.task = task
    def execute(self):
        self.task.do_something_1()
        self.task.do_something_2()

if __name__=='__main__':

    commands = [Command]
    commands.append(SimplePrintCommand('Starting an important Task'))
    commands.append(ComplexCommand(Taskset()))
    commands.append(SimplePrintCommand('Ending an important Task'))

    for command in commands:
        command.execute()
