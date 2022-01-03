# outside the function is called global variable
a = 10

def something():# this is inside the function is called local variable
    a = 15

    print("in fun " ,a)

something()



print("Outside", a)