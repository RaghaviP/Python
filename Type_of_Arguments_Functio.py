#2 Types of Argument are there:
# formal Arguments-when you define value it is formal Arguments
# Actual Arguments-when you pass or call the values is actual A.
# in actual 4 types are there
#position,keyword,Default,Variable Length.

'''
def add(a,b):#a,b is called as formal arguments
    c = a + b
    print(c)

add(5,6)#5,6 is called as actual argument here.


def person(name,age):
    print(name)#this is know as position argu
    print(age)

person('Leeminho',30)#calling by person to get ans


def person(name,age):
    print(name)
    print(age)

person(age = 30,name = "Leeminho")#here we used keyword argument where variable1 is age and vrbl 2 is name


def person(name,age=18):#if you are not passing value its default Argu.
    print(name)
    print(age)

person("Leeminho",30)


#Variable Length Argument
def sum(a,*b):# *b means where we can take or have multiple values.

    print(a)(5)
    print(b)(6,34,87,67,23)

sum(5,6,34,87,67,23)


def sum(*b):

    c = 0

    for i in b:
        c = c + i

    print(c)

sum(5,6,34,87,67,23)
'''