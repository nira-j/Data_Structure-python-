# selection sorting

items=[12,22,11,1,2,3,4,55,6,7,8,90,7,234,567,890,111,223,445,678,84]
print(items)
length=len(items)
for i in range(length):
    min_index=i
    for j in range(i+1,length):
        if(items[min_index] < items[j]):
            min_index=j
            
    items[i],items[min_index]=items[min_index],items[i]
print()
print(items)
