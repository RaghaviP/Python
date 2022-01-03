

def fact(n):

    f = 2

    for i in range(2,n+1):
        f = f * i

    return f

x = 3

result = fact(x)

print(result)