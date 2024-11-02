class Solution:
    def longestConsecutive(self, nums):
        longest = 0
        dic = {}

        for i in nums:
            dic[i] = True

        for num in nums:
            if num - 1 not in dic:
                cnt = 1
                target = num + 1
                while target in dic:
                    target += 1
                    cnt += 1
                longest = max(longest, cnt)
        return longest