import sys
input = sys.stdin.readline

a, b = input().split()

nums = "0123456789abcdefghijklmnopqrstuvwxyz"
count = 0
res = []

# 문자별 최대값 구하기ㄴ
# (주어진 문자보다 작은 진법으로는 변환할 수 없기 때문)
a_Max = nums.index(max(list(a)))
b_Max = nums.index(max(list(b)))


# notation진법으로 바뀐 num을 10진법으로 바꾸는 함수
def trans(num, notation):
    num = num[::-1]
    tmp = 0

    for i in range(len(num)):
        tmp += (int(notation)**i) * nums.index(num[i])

    return tmp


# 각 문자의 최대값 + 1 진법부터 36진법까지 값을 비교해서
# 결과가 같아지는 값을 기록해준다. 
for i in range(a_Max + 1, 37):
    for j in range(b_Max + 1, 37):
        if i == j:
            continue

        if trans(a, i) == trans(b, j):
            if trans(a, i) >= 2**63:
                continue

            res.append((trans(a, i), i, j))
            count += 1

if count == 1:
    print(*res[0])
elif count > 1:
    print("Multiple")
else:
    print("Impossible")