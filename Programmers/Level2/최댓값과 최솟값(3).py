def solution(s):
    nums = list(map(int, s.split(" ")))

    res = []
    res.append(min(nums))
    res.append(max(nums))

    return " ".join(map(str, res))

s ="1 2 3 4"
print(solution(s))
        