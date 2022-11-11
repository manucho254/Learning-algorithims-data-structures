import random
import sys
from load import load_numbers

"""
  Bogo sort
  A terrible sorting algorithim don't even bother using this
"""

numbers = load_numbers(sys.argv[1])

def is_sorted(values: list):
    for i in range(len(values) - 1):
        if values[i] > values[i + 1]:
            return False
    return True

print(is_sorted(numbers))

def bogo_sort(values):
    count = 0
    while not is_sorted(values):
        random.shuffle(values)
        count += 1
    print(count)
    return values

print(bogo_sort([1, 3, 5, 2, 6, 7, 8, 1]))

