rsp = '205'

def solution(rsp):
    res = ''

    for i in rsp:
        if i == '2':
            res += '0'
        elif i == '0':
            res += '5'
        else:
            res += '2'

    return res

print(solution(rsp))
