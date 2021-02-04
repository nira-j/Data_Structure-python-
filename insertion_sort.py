# insertion sort


items=[12,22,11,1,2,3,4,55,6,7,8,90,7,6,55,44,34,576,33,56,234,567,890,111,223,445,678,84]
print(items)

num=len(items)
for i in range(num):
    for j in range(i,0,-1):
        if(items[j]>items[j-1]):
            items[j],items[j-1]=items[j-1],items[j]

        if j==-1:
            break
print("After sorting....")
print(items)
