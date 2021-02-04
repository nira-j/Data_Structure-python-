# selection sorting
# Time complexity of selection sort is O(n^2) While space complexity is O(n).
# selection sort does not take extra memory space to sort elements in a list.

# list of item s to be sort
items=[12,22,11,1,2,3,4,55,6,7,8,90,7,234,567,890,111,223,445,678,84]
print(items)
length=len(items)
# len() return length of list
for i in range(length):
    min_index=i
    for j in range(i+1,length):
        if(items[min_index] < items[j]):
            min_index=j
            
    items[i],items[min_index]=items[min_index],items[i]
print()
print(items)

