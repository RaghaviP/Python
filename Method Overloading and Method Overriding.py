
class Student:

    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self,a=None,b=None,c=None):

        s = 0

        if a!=None and b!=None and c!=None:
            s = a +b+c
        elif a!=None and b!=None:
             s = a +b
        else:
            s = a

        return s

s1 = Student(85,36)

#print(s1.sum(5))

print(s1.sum(8,6,9))
'''

class A:

    def show(self):
        print("SAMSUNG BRAND")

class B:

    def show(self):
            print("its ASUS")

#class B(A):
   # pass

a1 = B()
a1.show()
'''
