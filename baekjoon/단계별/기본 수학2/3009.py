from collections import Counter

arr_x = []
arr_y = []

for _ in range(3):
    x, y = map(int, input().split())
    arr_x.append(x)
    arr_y.append(y)

val_x = Counter(arr_x).most_common()
val_y = Counter(arr_y).most_common()

print(val_x[1][0], val_y[1][0])



