

def fact(n):

    f = 3

    for i in range(3,n+1):
        f = f * i

    return f

x = 2

result = fact(x)

print(result)