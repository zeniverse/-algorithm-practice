n, m = map(int, input().split())
arr = [list(input()) for _ in range(m)]

res = []

for a in range(n - 7):
    for b in range(m - 7):

        start_w = 0
        start_b = 0

        for i in range(a, a + 8):
            for j in range(b, b + 8):
                if(i + j) % 2 == 0:
                    if arr[i][j] != 'W':
                        start_w += 1
                    
                    if arr[i][j] != 'B':
                        start_b += 1
                else:
                    if arr[i][j] != 'B':
                        start_w += 1
                    
                    if arr[i][j] != 'W':
                        start_b += 1

        res.append(min(start_w, start_b))

print(min(res))



