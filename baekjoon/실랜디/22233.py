import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
memo = {}
res = 0

for _ in range(n):
    memo[input().rstrip()] = 1
    res += 1


for _ in range(m):
    word = list(input().rstrip().split(","))
    
    for i in word:
        if i in memo.keys():
            if memo[i] == 1:
                memo[i] = 0
                res -= 1

    print(res)