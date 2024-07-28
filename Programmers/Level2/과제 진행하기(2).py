

def solution(plans):
    res = []

    for i in range(len(plans)):
        h, m = map(int, plans[i][1].split(":"))
        plans[i][1] = h * 60 + m
        plans[i][2] = int(plans[i][2])

    plans.sort(key=lambda x:x[1])
    stack = []

    for i in range(len(plans) - 1):
        stack.append(plans[i])
        gap = plans[i + 1][1] - plans[i][1]

        if stack[-1][2] <= gap:
            name, start, time = stack.pop()
            gap -= time
            res.append(name)
        else:
            stack[-1][2] -= gap
            gap = 0

    res.append(plans[-1][0])

    while stack:
        res.append(stack[-1][0])
        stack.pop(-1)

    return res

plans = [["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]
print(solution(plans))

