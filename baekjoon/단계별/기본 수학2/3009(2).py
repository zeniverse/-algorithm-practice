arr_x = []
arr_y = []

for _ in range(3):
    x, y = map(int, input().split())
    arr_x.append(x)
    arr_y.append(y)

for i in range(3):
    if arr_x.count(arr_x[i]) == 1:
        result_x = arr_x[i]
    
    if arr_y.count(arr_y[i]) == 1:
        result_y = arr_y[i]

print(result_x, result_y)

