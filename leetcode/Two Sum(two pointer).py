
def twoSum(nums, target):
    nums.sort() # O(nlogn)
    l, r = 0, len(nums) - 1

    while l < r:
        if nums[l] + nums[r] > target:
            r -= 1
        elif nums[l] + nums[r] < target:
            l += 1
        else:
            return True
    return False

nums = [2,7,11,15]
target = 4

print(twoSum(nums, target))
