sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]

for i in range(len(sizes)):
    if sizes[i][0] < sizes[i][1]:
        sizes[i] = [sizes[i][1], sizes[i][0]]


x = max(sizes, key=lambda x: x[0])[0]
y = max(sizes, key=lambda x: x[1])[1]

print(x*y)