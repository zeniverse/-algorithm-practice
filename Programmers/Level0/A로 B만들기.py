
before = "allpe"
after = "apple"

def solution(before, after):
    a = list(after)
    b = list(before)

    a.sort()
    b.sort()

    if a == b:
        return 1
    else:
        return 0

print(solution(before, after))
