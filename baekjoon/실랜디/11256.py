
for _ in range(int(input())):
    j, n = map(int, input().split())
    boxes = []
    count = 0

    for _ in range(n):
        r, c = map(int, input().split())
        boxes.append(r * c)

    boxes.sort(reverse=True)

    for i in boxes:
        count += 1
        j -= i
        
        if j <= 0:
            break

    print(count)
