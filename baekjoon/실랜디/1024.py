n, l = map(int, input().split())

# (x + 1) + (x + 2) + ... + (x + i) = ix + (1 + 2 + 3 + 4+ ... + i)
# = ix + i(i + 1) / 2 = n
#  ix = n - i(i + 1)/2
#  x = n/i - (i + 1)/2
# 자연수의 합이므로 x는 정수이고, x + 1은 0이상이어야 한다

for i in range(l, 101):
    x = n/i - (i+1)/2

    if int(x) == x:
        x = int(x)
        if x + 1 >= 0:
            for j in range(x+1, x+i+1):
                print(j, end=" ")
            break
else:
    print(-1)