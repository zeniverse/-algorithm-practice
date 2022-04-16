n = int(input())
n_copy = n
cnt = 0

if n < 10:
    n = int('0'+str(n))

while True:

    a = n // 10
    b = n % 10
    c = (b * 10) + ((a+b)%10)
    
    print(a, b, c, n, cnt)

    cnt += 1
    
    if c == n_copy:
        print(cnt)
        break

    n = c