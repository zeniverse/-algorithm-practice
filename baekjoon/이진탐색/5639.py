
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def postOrder(nums):
    length = len(nums)

    if length <= 1:
        return nums

    for i in range(1, length):
        if nums[i] > nums[0]:
            return postOrder(nums[1:i]) + postOrder(nums[i:]) + [nums[0]]

    return postOrder(nums[1:]) + [nums[0]]

arr = []

while True:
    try:
        arr.append(int(input()))
    except:
        break

arr = postOrder(arr)

for i in arr:
    print(i)