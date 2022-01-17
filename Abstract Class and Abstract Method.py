from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):
    def process(self):
        print("its running")

class WhiteBoard:
    def write(self):
        print("Writing on board")

class Programmer:
    def work(self,com):
        print("Solving Bugs")
        com.process()


#com = Computer()
com1 = Laptop()
#com.process()
prog1 = Programmer()
prog1.work(com1)

#com1.process()

