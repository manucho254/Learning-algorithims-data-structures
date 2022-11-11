def sum(nums):
    if not nums:
        return 0
    print("calling sum (%s)" % nums[1:])
    remaining_sum = sum(nums[1:])
    print("calling sum (%s) returning %d + %d" % (nums, nums[0], remaining_sum))
    return nums[0] + remaining_sum

print(sum([1, 2, 7, 9, 100, 80]))
