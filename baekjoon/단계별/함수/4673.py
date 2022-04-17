def check(num):
    next = num

    for i in str(next):
        next += int(i)
    
    return next


total_num = set(range(1, 10001))
d_num = set()

for num in total_num:
    d_num.add(check(num))

res = sorted(total_num - d_num)
[print(i) for i in res]