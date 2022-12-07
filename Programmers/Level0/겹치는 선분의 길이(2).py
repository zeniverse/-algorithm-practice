
lines = [[0, 5], [3, 9], [1, 10]]

def solution(lines):
    sets = [set(range(min(l), max(l))) for l in lines]
    return len(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])
    

print(solution(lines))