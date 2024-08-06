

def solution(priorities, location):
    priorities = [(i, p) for i, p in enumerate(priorities)]
    answer = 0

    while True:
        cur = priorities.pop(0)
        if any(cur[1] < p[1] for p in priorities):
            priorities.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer

priorities = [1, 1, 9, 1, 1, 1]
location = 0
print(solution(priorities, location))