
msg = 'KAKAO'

def solution(msg):
    answer = []
    arr = [chr(i) for i in range(65, 91)]
    
    start = 0
    end = start + 1
    
    while end <= len(msg):
        if msg[start:end] in arr:
            end += 1
        else:
            answer.append(arr.index(msg[start:end-1]) + 1)
            arr.append(msg[start:end])
            start = end - 1
            
    answer.append(arr.index(msg[start:end]) + 1)
    return answer

print(solution(msg))