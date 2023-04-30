
def solution(binomial):
    a, c, b = binomial.split(" ")
    if c == '+':
        return int(a) + int(b)
    elif c == "-":
        return int(a) - int(b)
    else:
        return int(a) * int(b)

binomial = "43 + 12"
print(solution(binomial))