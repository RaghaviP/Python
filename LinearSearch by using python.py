pos = -1

def search(List, n):
    i = 0

    while i< len(List):
        if List [i] == n:
           globals() ['pos'] = i
           return True
        i = i + 1

        return False

List = [5, 8, 9, 2, 6]
n = 5

if search(List, n):
    print("Found at ",pos+1)
else:
    print("Not Found")