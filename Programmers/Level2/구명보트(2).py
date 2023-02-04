
def solution(people, limit):
    res = 0
    people.sort()

    start = 0
    end = len(people) - 1

    while start < end:
        if people[start] + people[end] <= limit:
            start += 1
            res += 1
        end -= 1

    return len(people) - res



people = [70, 80, 50]
limit = 100
print(solution(people, limit))





