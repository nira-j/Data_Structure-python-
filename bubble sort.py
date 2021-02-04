# bubble sorting
# Time complexity for bubble sort is O(n^2) ad sace complexity is O(n).
# Bubble sort does not take extra space for sorting elements of list.

# List of items to be sorted 
items=[12,22,11,1,2,3,4,55,6,7,8,90,7,6,55,44,34,576,33,56,234,567,890,111,223,445,678,84]
print(items)
length=len(items)
# len() method returns number of elements in a list
 
for i in range(length-1):
    for j in range(length-i-1):
        if(items[j] > items[j+1]):
            items[j],items[j+1]=items[j+1],items[j]


print("After sorting...")
print(items)
