

class Computer:

    def __init__(self):
        self.name = "Ria"
        self.age = 28

    def update(self):
        self.age = 30

    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False

c1 = Computer()
c1.age = 30
c2 = Computer()

if c2.compare(c1):
    print("They are equal")
else:
    print("They are different")

c1.name = "Encato"
c2.age = 28

c1.update(),c2.update

print(c1.name,c2.name)