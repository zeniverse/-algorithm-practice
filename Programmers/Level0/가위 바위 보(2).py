rsp = '205'

def solution(rsp):
    dic = {'0':'5', '2':'0', '5':'2'}
    return ''.join(dic[i] for i in rsp)

print(solution(rsp))
