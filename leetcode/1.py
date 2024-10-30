class Solution:
    def twoSum(self, nums, target):
        dic = {}

        for i, num in enumerate(nums):
            needed = target - num
            if needed in dic:
                return [dic[needed], i]
            dic[num] = i