class Solution:
    def longestConsecutive(self, nums):
        res = 0

        if not nums:
            return res
        
        dic = {x : x + 1 for x in nums}
        for n in nums:
            target = n
            cnt = 0

            if n - 1 not in dic:
                while target in dic:
                    target = dic[target]
                    cnt += 1
                res = max(res, cnt)
        return res
