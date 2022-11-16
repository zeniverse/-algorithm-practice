import sys
input = sys.stdin.readline

def check(n):
    ans = n

    for i in str(ans):
        ans += int(i)
        
    return ans


arr = set(range(1, 10001))
d_num = set()

for num in arr:
    d_num.add(check(num))
    
res = sorted(arr - d_num)

for i in res:
    print(i)