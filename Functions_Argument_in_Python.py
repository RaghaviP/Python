'''
def update(x):
    x = 8
    print(x)

update(10)


def update(lst):

    print(id(lst))

    lst[1] = 25
    print(id(lst))
    print("x ", lst)

lst = [10,20,30]
print(id(lst))
update(lst)
print("1st ", lst)
'''