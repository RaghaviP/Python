def sort(sun):
    for w in range(len(sun)-1,0,-1):
        for j in range(w):
            if sun[j]>sun[j+1]:
                temp = sun[j]
                sun[j]=sun[j+1]
                sun[j+1]=temp

sun = [8, 6, 2, 9, 3]
sort(sun)

print(sun)