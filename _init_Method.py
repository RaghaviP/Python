#special method using _init_.
#we use init to instialize the variables.

class computer:

    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("config is ", self.cpu, self.ram)

com1 = computer('i5', 16)
com2 = computer('Ryzen 3',8)

com1.config()
com2.config()



