pos = -1

def search(List,n):

    l = 0
    u = len(List)-1

    while 1 <= u:
        mid = (l+u) // 2 # // is used for integer Division

        if List[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if List[mid] < n:
                l = mid+1
            else:
                u = mid-1

        return False

List = [1,2,3,4,5,6,7,8,9,855,8555,9944895]
n = 10

if search(List, n):
    print("Found at ", pos+1)
else:
    print("Not Found")
