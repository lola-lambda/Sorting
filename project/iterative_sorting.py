# Complete the selection_sort() function below in class with your instructor
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        # find next smallest element
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # swap
        smallest = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = smallest

    return arr
# runtime: O(n**2)

# TO-DO: implement the Insertion Sort function below
def insertion_sort(arr):
    # for each item in the array, compare it to previous items and insert it in front of the item it is greater than
    for i in range(1, len(arr)):
        index = i
        cur = arr[i]
        while index > 0 and arr[index - 1] > cur:
            arr[index] = arr[index - 1]
            index -= 1
        arr[index] = cur
    return arr

# STRETCH: implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr


print('selection', selection_sort([6,5,2,1,8,19]))
print('insertion', insertion_sort([6,5,2,1,8,19]))
# print('bubble', bubble_sort([6,5,2,1,8,19]))
# print('count', count_sort([6,5,2,1,8,19]))