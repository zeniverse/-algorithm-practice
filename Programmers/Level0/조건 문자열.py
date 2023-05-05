
def solution(ineq, eq, n, m):
    return int(eval(str(n) + ineq + eq.replace("!", "") + str(m)))

ineq = ">"
eq = "!"
n = 41
m = 78
print(solution(ineq, eq, n, m))