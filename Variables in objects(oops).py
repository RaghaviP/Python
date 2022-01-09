
class Car:
    #static or class nampspace or variable.
    wheel = 4


    def __init__(self):
        #instance namespace or variable.
        self.mil = 20
        self.company = "Range Grover"

A1 = Car()
A2 = Car()

A1.mil = 8

Car.wheels = 6

print(A1.company, A1.mil, A1.wheels)
print(A2.company, A2.mil, A2.wheels)