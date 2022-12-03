
age = 23

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
def solution(age):
    res = ''

    for i in str(age):
        res += alpha[int(i)]
        
    return res


print(solution(age))
