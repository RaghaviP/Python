def topten():

    n = 1

    while n <= 10:
        sq = n*n
        yield sq
        n += 1

values = topten()

for x in values:
    print(x)