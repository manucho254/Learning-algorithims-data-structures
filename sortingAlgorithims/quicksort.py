"""
  Quicksort sort
  worst case O(n^2)
  A medium good sorting algorithim
"""

numbers = [15, 7, 3, 9, 10, 5]

def quicksort(values):
    # base case
    if len(values) <= 1:
        return values
    
    less_than_pivot = []
    greater_than_pivot = []
    pivot = values[0]
    
    for value in values[1:]:
        if value <= pivot:
            less_than_pivot.append(value)
        else:
            greater_than_pivot.append(value)
    
    print(quicksort(less_than_pivot), quicksort(greater_than_pivot))
    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)
    
sorted_numbers = quicksort(numbers)

print(sorted_numbers)