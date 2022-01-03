
def count(lst):
    even = 0
    odd = 0

    for i in lst:
        if i % 2 == 0:
              even += 1
        else:
            odd += 1
    return even,odd

lst = [25,5,78,64,85,94,25,64,78,24,]

even, odd = count(lst)

print("Even : {} and Odd : {}".format(even,odd))
