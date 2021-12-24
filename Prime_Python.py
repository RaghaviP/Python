'''
mylist = [2,5,65,25,]

prime =[]

for i in mylist:
    c = 0

    for j in range(1,i):
        if i % j == 0:
            c += 1

    if c == 1:
            prime.append(i)

print(prime)
'''