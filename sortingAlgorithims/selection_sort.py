"""
  selection sort
  O(n^2)
  A medium good sorting algorithim
"""

import random

arr = []
n = 0
while n != 10000:
    val = random.randint(1, 10001)
    arr.append(val)
    n = val
print(arr)

# my hacky solution
def selection_sort(values: list) -> list:
    sorted_ = []
    while len(values) > 0:
        for val in values:
            if val == min(values):
                sorted_.append(val)
                values.remove(val)
        print("%-25s        %-25s" % (values, sorted_))
    return sorted_
                
print(selection_sort([1, 4, 2, 5, 3, 7, 9, 6, 8, 1, 2]))
print(selection_sort(["milk", "egg", "bread"]))
print(selection_sort(arr))


#schools solution

def selection_sort_2(values: list) -> list:
    sorted_list = []
    print("%-25s       %-25s" % (values, sorted_list))
    for _ in range(0, len(values)):
        index_to_move = index_of_min(values)
        sorted_list.append(values.pop(index_to_move))
        
    return sorted_list

def index_of_min(values):
    min_index = 0
    for i in range(1, len(values)):
        if values[i] < values[min_index]:
            min_index = i
            
    return min_index

print(selection_sort_2([1, 4, 2, 5, 3, 7, 9, 6, 8, 1, 2]))
print(selection_sort(["milk", "egg", "bread"]))

