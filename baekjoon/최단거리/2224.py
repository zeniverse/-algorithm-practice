import sys
input = sys.stdin.readline

graph = [[0] * 58 for _ in range(58)]
count = 0

for _ in range(int(input())):
    con = input()
    if con[0] == con[5]:
        continue

    if not graph[ord(con[0]) - 65][ord(con[5]) - 65]:
        graph[ord(con[0]) - 65][ord(con[5]) - 65] = 1
        count += 1

for k in range(58):
    for a in range(58):
        for b in range(58):
            if a != b and not graph[a][b] and graph[a][k] and graph[k][b]:
                graph[a][b] = 1
                count += 1


print(count)
for i in range(58):
    for j in range(58):
        if graph[i][j]:
            print(chr(i + 65) + " => " + chr(j + 65))

