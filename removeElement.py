def elm(nums, val):
    for i in range(len(nums)):
        if val == nums[i]:
            nums.pop(i)
    k = len(nums)
    return k


print(elm([3,2,2,3], 2))