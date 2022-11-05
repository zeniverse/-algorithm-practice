def solution(n, times):
    answer = 0
    start = 0
    end = max(times) * n
    
    while start <= end:
        mid = (start + end) // 2
        people = 0
        
        for t in times:
            people += mid // t
            
            if people >= n:
                break
                
        if people < n:
            start = mid + 1
        else:
            answer = mid
            end = mid - 1
            
    
    return answer

print(solution(6, [7, 10]))
    