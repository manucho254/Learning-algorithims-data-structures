def merge_sort(array: list):
    """
    sorts a list in ascending order
    Returns a new sorted list
    
    Devide: Find the endpoint of the list and divide into sublists
    Conquer: Recursively sort the sublists created in previous step
    Combine: Merge the sorted sublists created in previous step
    
    Takes overall O(n log n) in the worst case
    
    """
    
    if len(array) <= 1:
        return array
    
    left_half, right_half = split(array)
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    
    return merge(left, right)

def split(array: list):
    """ 
    Devide the unsorted list at midpoint into sublists
    Returns two sublists - left and right
    
    Takes overall O(K log n) logarithmic time
    
    It takes  O(K log n) because of the usage 
    of slicing in this implimentation
    
    But takes O(log n) while using a recursive solution
    
    """
        
    mid = len(array) // 2
    
    left = array[:mid]
    right = array[mid:]
    
    return left, right
    
    
def merge(left: list, right: list):
    """
        Merges two list (arrays), sorting them in the process
        Returns a new merged list
        
        Runs in Ovarall O(n) linear time
    """
    l =  []
    i = 0
    j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1
    
    while j < len(right):
        l.append(right[j])
        j += 1
        
    return l

def verify_sorted(array):
    n = len(array)
    
    if n == 0 or n == 1:
        return True
    
    return array[0] < array[1] and verify_sorted(array[1:])

numbers = [3, 1, 4, 2, 5, 7, 9, 6, 10, 8]
print(merge_sort(numbers))
print(verify_sorted(numbers))
print(verify_sorted(merge_sort(numbers)))
    