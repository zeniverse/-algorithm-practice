
import sys
input = sys.stdin.readline

n = int(input())
arr = []
res = 0

for _ in range(n):
    power, weight = map(int, input().rstrip().split())
    arr.append([power, weight])

def dfs(depth):
    global res

    if depth == n:
        count = 0
        for i in arr:
            if i[0] <= 0:
                count += 1
        if res < count:
            res = count
        return

    # 현재 쥐고있는 계란이 깨진 경우 -> 다음 계란으로 이동
    if arr[depth][0] <= 0:
        dfs(depth + 1)

    else:
        flag = False
        for i in range(n):
            if i != depth and arr[i][0] > 0:
                flag = True
                arr[depth][0] -= arr[i][1]
                arr[i][0] -= arr[depth][1]
                dfs(depth + 1)
                arr[depth][0] += arr[i][1]
                arr[i][0] += arr[depth][1]
        
        # 달걀이 전부 깨져있을 경우엔 depth == n 을 만들어줘서
        # 깨진 달걀의 갯수를 확인하고 return 할 수 있게 해준다
        if not flag:
            dfs(n)

dfs(0)
print(res)