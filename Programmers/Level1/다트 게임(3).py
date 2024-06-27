
dartResult = '1D2S#10S'

def solution(dartResult):
    arr = []
    tmp = ''
    
    for i in dartResult:
        if i == 'S':
            arr.append(int(tmp))
            tmp = ''
        elif i == 'D':
            arr.append(int(tmp) ** 2)
            tmp = ''
        elif i == 'T':
            arr.append(int(tmp) ** 3)
            tmp = ''
        elif i == '*':
            if len(arr) == 1:
                arr[0] *= 2
            else:
                arr[-1] *= 2
                arr[-2] *= 2
        elif i == '#':
            arr[-1] *= -1
        else:
            tmp += i
        
    return sum(arr)

print(solution(dartResult)) 

