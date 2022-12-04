
before = "allpe"
after = "apple"

def solution(before, after):
    before = sorted(before)
    after = sorted(after)

    if after == before:
        return 1
    else:
        return 0

print(solution(before, after))
