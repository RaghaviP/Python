'''
class person:
    def __init__(self, name, id):
        self.name = name
        self.age = id

    def sayHello(self):
        print("Hello! My name is  " + self.name)

p1 = person("ShriRam", 135)
p1.sayHello()
'''

class student:
     school = 'IGV'

     def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

     def avg(self):
        return(self.m1 + self.m2)/2

     @classmethod
     def getschool(cls):
        return cls.school

     @staticmethod
     def info():
        print("This is University")

s1 = student(34,54,)
s2 = student(65,85,)

print(s1.avg())
print(student.getschool())

student.info()




