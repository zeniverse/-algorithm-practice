k = int(input())
arr = []
x, y = [], []
arr2 = []

for i in range(6):
    num, dist = map(int, input().split())
    arr.append((num, dist))

    if arr[i][0] == 3 or arr[i][0] == 4:
        x.append(arr[i][1])
    elif arr[i][0] == 1 or arr[i][0] == 2:
        y.append(arr[i][1])


# 입력된 방향 중 하나를 건너띄고 양옆의 방향이 같다면
# 건너띈 값이 빼야될 도형의 가로세로 길이가 된다
for i in range(6):
    if arr[i][0] == arr[(i + 2) % 6][0]:
        arr2.append(arr[(i + 1) % 6][1])

print(((max(x) * max(y)) - (arr2[0] * arr2[1])) * k)