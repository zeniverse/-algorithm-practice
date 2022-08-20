from opcode import hasname


n = 2

res = []

def hanoi(n, start, goal, help):
    if n == 1:
        res.append([start, goal])
        return

    hanoi(n - 1, start, help, goal)
    res.append([start, goal])
    hanoi(n - 1, help, goal, start)

hanoi(n, 1, 3, 2)
print(res)



