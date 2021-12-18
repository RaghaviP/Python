
'''
def greet():# this is function defination
    print("Python is Programing Language")
    print("It is Interpret Language")

greet()# this is called as calling


def greet():
    print("How's it going?")

greet()


def add(a,b):# I have passed 2 arguments a, b
    D = a + b
    print(D)

add(10,15)


def sub(e,f):
    G = e + f
    print(G)

sub(458,654)


def mult(h,i):
    j = h * i
    print(j)

mult(15,4)


def div(k,l):
    m = k / l
    print(m)

div(45,8)


def add_sub(x,y):
    z = x + y
    a = x - y
    return z,a

result1,result2 = add_sub(45,98)
print(result1,result2)


def mult_div(a,b):
    c = a * b
    d = a / b
    return c,d

result1,result2 = mult_div(10,60)
print(result1,result2)


def add_sub_mult_div(e,f):
    g = e + f
    h = e - f
    i = e * f
    j = e / f
    return g,h,i,j

result1,result2,result3,result4 = add_sub_mult_div(5,25)
print(result1,result2,result3,result4 )


def update(x):
    x = 20
    print(x)

update(10)


def update(lst):

    print(id(lst))

    lst[3] = 20
    print(id(lst))
    print("lst ", lst)


lst = [50,60,70,80]
print(id(lst))
update(lst)
print("lst ", lst)


def add(a,b):#this is formal argument
    c = a + b
    print(c)

add(5,6)#this is acutal argument


def person(name,height):
    print(name)
    print(height)

person("lisa",175)

#keword argument
def person(name,height):
    print(name)
    print(height)

person(height = 175, name = "lisa")


#Default argument

def person(name,height = 149):
    print(name)
    print(height)

print("lisa", 175)


#variable Length argument- we can define a function where no arguments are not fixed.

def sum(a, *b):

   c = 0

   for i in b:
       c = c + i

   print(c)

sum(5,58,56,2,6)


def myfun(*argv):

    for arg in argv:
        print(arg)

myfun("Hello", "Welcome", "to", "Besant")


def mylife(*argv):

    for arg in argv:
        print(arg)

mylife("I ", "want", "to","be", "Data Analyst", "and", "Data Scientist")
'''

def mydream(*argv):

    for arg in argv:
        print(arg)

mydream("I", "want", "to", "be","a", "Python Developer")

