from itertools import permutations
import sys

input = sys.stdin.readline

n = int(input())
arr = list(permutations(list(range(1, 10)), 3))

for _ in range(n):
    num, s, b = map(int, input().split())
    tmp = []

    for check in arr:
        count_s, count_b = 0, 0

        for i, str_num in enumerate(str(num)):
            if int(str_num) == check[i]:
                count_s += 1
            if int(str_num) != check[i] and int(str_num) in check:
                count_b += 1

        if s == count_s and b == count_b:
            tmp.append(check)

    arr = tmp
    
print(len(arr))