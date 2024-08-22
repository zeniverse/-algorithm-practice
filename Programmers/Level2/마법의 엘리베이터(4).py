
storey = 2554

def solution(storey):
    # 일의 자리 수를 구해서 해당 숫자가 5보다 크면 위로 올라가는게 더 빠릑 때문에 10 - btn 만큼 더하고,
    # 5보다 작으면 내려가는게 더 빠르므로 btn 만큼 더한다
    
    # 만약에 5라면, 그 앞자리 수를 구해 비교하며 계산해서 일의자리 숫자를 0으로 맞춘다
    # ex) storey가 195 -> 그다음 숫자가 9이기 때문에 위로 올라가면 10의 배수가 됨
    # 따라서 처음 btn이 5라면 그 전 숫자를 확인해야 한다
    answer = 0

    while storey > 0:
        btn = storey % 10

        if btn > 5:
            answer += (10 - btn)
            storey += (10 - btn)
        elif btn < 5:
            answer += btn
            storey -= btn
        else:
            tmp = storey // 10
            if tmp % 10 >= 5:
                answer += (10 - btn)
                storey += (10 - btn)
            else:
                answer += btn
                storey -= btn
        storey //= 10
    return answer
print(solution(storey))