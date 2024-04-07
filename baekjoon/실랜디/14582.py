a = list(map(int, input().split()))
b = list(map(int, input().split()))

flag = False
a_sum, b_sum = 0, 0

for i in range(9):
    a_sum += a[i]
    if a_sum > b_sum:
        flag = True
    b_sum += b[i]

if sum(a) < sum(b) and flag:
    print("Yes")
else:
    print("No")