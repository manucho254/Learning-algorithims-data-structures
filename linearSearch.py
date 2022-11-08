arr = [x for x in range(1, 11)]

def linear_search(array: list,  target: int) -> int:
    """
       Return the index position of the target if found, else returns None
    """
    for x, i in enumerate(array):
        if i == target:
            return x
    return 0

def verify(index: int):
    if index != 0:
        print("Target found at index {}".format(index))
    else:
        print("Target found not found")
        
verify(linear_search(arr, 10))