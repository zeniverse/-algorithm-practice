import sys
input = sys.stdin.readline

arr = []

for _ in range(int(input())):
    count = 0
    s = input().rstrip()

    for i in s:
        if i.isdigit():
            count += int(i)

    arr.append((s, count))

arr.sort(key=lambda x: (len(x[0]), x[1], x[0]))

for i in arr:
    print(i[0])

        
