class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        
        nums = list(set(nums))
        nums.sort()

        arr = []
        cnt = 1
        y = nums[0]

        for i in nums[1:]:
            if y + 1 != i:
                arr.append(cnt)
                cnt = 0
            y = i
            cnt += 1
        arr.append(cnt)

        return max(arr)