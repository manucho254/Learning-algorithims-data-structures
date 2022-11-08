""" All the values must be sorted """
arr = [x for x in range(1, 10000000001)]

def binary_search(array: list,  target: int) -> int:
    first = 0
    last = len(array) - 1
    
    while first <= last:
        midpoint = (first + last) // 2
        if array[midpoint] == target:
            return midpoint
        elif array[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
            
    return 0

def verify(index: int):
    if index != 0:
        print("Target found at index {index}".format(index=index))
    else:
        print("Target found not found")
        
verify(binary_search(arr, 10))