# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

    if len(arr) == 0:
        return -1 # array empty
    
    low = 0
    high = len(arr)-1
    
    while low < high:
        middle = (low+high)//2
        if target is arr[middle]:
            return middle
        if target < arr[middle]:
            high = middle
        elif target > arr[middle]:
            low = middle

    return -1 # not found
# runtime complexity: O(logn)

# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):

    if len(arr) == 0:
        return -1 # array empty
    
    middle = (low+high)//2

    if target == arr[middle]:
        return middle
    elif target < arr[middle]:
        return binary_search_recursive(arr, target, low, middle)
    else:
        return binary_search_recursive(arr, target, middle, high)

print('linear', linear_search([6,5,2,1,8,19], 8))
print('iterative binary', binary_search([6,5,2,1,8,19], 8))
print('recursive binary', binary_search_recursive([6,5,2,1,8,19], 8, 0, 5))