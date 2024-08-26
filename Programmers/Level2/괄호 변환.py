
p = "(()())()"

def solution(p):

    def divide(li):
        opencnt = 0
        closecnt = 0

        for i in li:
            if i == '(':
                opencnt += 1
            else:
                closecnt += 1

            if opencnt == closecnt:
                u = li[:opencnt + closecnt]
                v = li[opencnt + closecnt: ]
                return u, v
            
    def check(li):
        stack = []
        for i in li:
            if i == '(':
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                else:
                    return False
        return True
    

    def newStr(u, v):
        result.append('(')
        process(v)
        result.append(')')

        del u[0]
        del u[-1]
        
        for i in u:
            if i == '(':
                result.append(')')
            else:
                result.append('(')

    def process(li):
        if len(li) == 0:
            return
        
        u, v = divide(li)

        if check(u):
            result.extend(u)
            process(v)
        else:
            newStr(u, v)

    result = []
    process(list(p))

    return ''.join(result)


print(solution(p))