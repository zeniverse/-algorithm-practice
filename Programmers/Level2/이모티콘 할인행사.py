from itertools import product


def solution(users, emoticons):
    res = [0, 0]
    cases = [10, 20, 30, 40]

    for case in product(cases, repeat=len(emoticons)):
        # 매출액, 플러스 가입 수
        total_pay, plusMember = 0, 0 

        for rate, price in users:
            # user가 지불할 금액
            pay = 0

            for idx, emoticon in enumerate(emoticons):
                if case[idx] >= rate:
                    # 주어진 할인율로 할인한 이모티콘 값을 지불할 금액에 더해주기
                    pay += emoticon * (100 - case[idx]) // 100
            
            # user에게 주어진 금액보다 크다면, 이모티콘 플러스 가입(구매를 취소하고 플러스에 가입하기 때문에 매출액 증가x)
            # user에게 주어진 금액보다 작다면, 매출액 증가
            if pay >= price:
                plusMember += 1
            else:
                total_pay += pay

        # 플러스 가입자가 많은게 우선이고, 가입자가 같다면 매출액이 높은게 우선 이기 때문에
        # 플러스 가입자가 많다면, res 리스트 초기화
        # 플러스 가입자는 같은데 매출액이 높다면, 매출액만 변경해주면 된다
        if res[0] < plusMember:
            res = [plusMember, total_pay]
        elif res[0] == plusMember and res[1] < total_pay:
            res[1] = total_pay

    return res

users = [[40, 10000], [25, 10000]]
emoticons = [7000, 9000]

print(solution(users, emoticons))