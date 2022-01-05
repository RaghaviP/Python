# start
#using Decorators will add extra features in the existing function.
#take div as the function for decorators.
#inner function def var is a,b.
#passing div fun with smart div fun.
#pass the value.2,4
#end program.
'''
def div(a,b):
    print(a/b)

def smart_div(func):

    def inner(a,b):
        if a < b:
            a,b = b,a
        return func(a,b)

    return inner

div = smart_div(div)

div(2,4)
'''

def div (x,y):
    print(x/y)

def smart_div(func):

    def inner (x,y):
        if x < y:
            x,y = y,x
        return func(x,y)

    return inner

div = smart_div(div)

div(3,9)



