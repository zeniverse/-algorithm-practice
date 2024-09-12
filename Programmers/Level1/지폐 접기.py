def solution(wallet, bill):
    answer = 0
    w_min = min(wallet)
    w_max = max(wallet)
    
    while min(bill) > w_min or max(bill) > w_max:
        if bill[0] > bill[1]:
            bill[0] //= 2
        else:
            bill[1] //= 2
        answer += 1
        
    return answer

wallet, bill = [30, 15], [26, 17]

print(solution(wallet, bill))

