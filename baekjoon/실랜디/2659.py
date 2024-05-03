arr = list(input().split())

def get_num(n):
    min = int(''.join(n))

    for i in range(1, 4):
        tmp = int(''.join(n[i:] + n[:i]))
        if min > tmp:
            min = tmp

    return min


clock_num = get_num(arr)
res = 1

for i in range(1111, clock_num):
    if '0' not in list(str(i)) and i == get_num(list(str(i))):
        res += 1

print(res)