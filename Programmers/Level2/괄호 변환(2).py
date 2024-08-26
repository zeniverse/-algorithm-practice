
p = "(()())()"

def divide(p):
    opencnt = 0
    closecnt = 0

    for idx, s in enumerate(p):
        if s == "(":
            opencnt += 1
        else:
            closecnt += 1

        if opencnt == closecnt :
            return p[:idx + 1], p[idx + 1:]
        
def check(u):
    stack = []

    for i in u:
        if i == "(":
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()
    return True

def solution(p):

    if not p:
        return ""
    
    u, v = divide(p)

    if check(u):
        return u + solution(v)
    else:
        answer = "("
        answer += solution(v)
        answer += ")"

        u = u[1:len(u) - 1]
        for i in u:
            if i == "(":
                answer += ')'
            else:
                answer += '('
    
    return answer


print(solution(p))