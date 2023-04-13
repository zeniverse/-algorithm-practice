

def solution(plans):
    res = []

    for i in range(len(plans)):
        h, m = map(int, plans[i][1].split(":"))
        start = h * 60 + m
        plans[i][1] = start
        plans[i][2] = int(plans[i][2])

    plans.sort(key=lambda x:x[1])
    stack = []

    for i in range(len(plans)):
        if i == len(plans) - 1:
            stack.append(plans[i])
            break

        sub, start, time = plans[i]
        nsub, nstart, ntime = plans[i + 1]

        if start + time <= nstart:
            res.append(sub)
            time_tmp = nstart - (start + time)

            while time_tmp != 0 and stack:
                tsub, tstart, ttime = stack.pop()
                if time_tmp >= ttime:
                    res.append(tsub)
                    time_tmp -= ttime
                else:
                    stack.append([tsub, tstart, ttime - time_tmp])
                    time_tmp = 0
        else:
            plans[i][2] = time - (nstart - start)
            stack.append(plans[i])

    while stack:
        plan = stack.pop()
        res.append(plan[0])

    return res

plans = [["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]
print(solution(plans))

