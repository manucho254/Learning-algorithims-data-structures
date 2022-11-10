import sys
# from load import load_numbers

"""
  selection sort
  A mdeium good algorithim
"""

# numbers = load_numbers(sys.argv[1])

# my solution
def selection_sort(values: list) -> list:
    sorted_ = []
    while len(values) > 0:
        for val in values:
            if val == min(values):
                sorted_.append(val)
                values.remove(val)
        print("%-25s                   %-25s" % (values, sorted_))
    return sorted_
                
print(selection_sort([1, 4, 2, 5, 3, 7, 9, 6, 8, 1, 2]))


#schools solution

def selection_sort_2(values: list) -> list:
    sorted_list = []
    
    print("%-25s                   %-25s" % (values, sorted_list))
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

