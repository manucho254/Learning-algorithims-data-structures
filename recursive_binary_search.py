""" The array must be sorted first before first for the array to work correctly"""

arr = [x for x in range(1, 1000000001)]

def recursive_binary_search(array:list, target:int) -> bool:
    if len(array) == 0:
        return False
    
    midpoint = len(array) // 2
    
    if array[midpoint] == target:
        return True
    
    #checking if the midpoint is less than target
    if array[midpoint] < target:
        return recursive_binary_search(array[midpoint+1:], target)
    
    #else executing this if the midpoint is greater than target
    return recursive_binary_search(array[:midpoint-1], target)


def verify(result: bool):
    print("Target found", result)
    
verify(recursive_binary_search(arr, 100))