

x = 15
print(id(x))

def code():
    x = 9

    a = globals() ['x']
    print(id(a))
    print("it is Working!! " , x)

    globals() ['a'] = 20



code()