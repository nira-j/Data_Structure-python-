# linear search algorithm is a simplest search algorithm.
# time complexity of linear search algorith is O(n), where n is the total no. of elements. 
# let a list of numbers
 


def linear_search(items,search_item):
    num=len(items) 
    # len() returns no. of elements in list "items"

    for i in range(num):
        if search_item==items[i]:
            return i+1

    return -1
        
if __name__=='__main__':
    items=[11,22,3,44,55,6,77,88,11,66,54,67,81,97,65]
    search_item=int(input("Enter a number to be search: "))
    result=linear_search(items,search_item)
    if result >= 0:
        print("searching item is present in given list at position {0}".format(result))
    elif result==-1:
        print("searching item is not present in given list")