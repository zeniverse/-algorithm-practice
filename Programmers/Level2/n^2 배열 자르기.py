
n = 4
left = 7
right = 14

arr = []

x = (left // n) + 1
y = (left % n) + 1

end_x = (right // n) + 1
end_y = (right % n) + 1


while True:

    if x == end_x and y == end_y:
        arr.append(max(x, y))
        break

    arr.append(max(x, y))

    y += 1

    if y >= n + 1:
        y %= n
        x += 1

print(arr)