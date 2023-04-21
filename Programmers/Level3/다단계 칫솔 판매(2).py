def find(parents, money, number, res):
    if parents[number] == number or money // 10 == 0:
        res[number] += money
        return
    
    send = money // 10
    mine = money - send
    res[number] += mine
    find(parents, send, parents[number], res)
    return


def solution(enroll, referral, seller, amount):
    n = len(enroll)
    res = [0] * (n + 1)
    d = {}
    parents = [i for i in range(n  + 1)]

    for i in range(n):
        d[enroll[i]] = i + 1

    for i in range(n):
        if referral[i] == '-':
            parents[i + 1] = 0
        else:
            parents[i + 1] = d[referral[i]]

    for i in range(len(seller)):
        find(parents, amount[i] * 100, d[seller[i]], res)
    
    return res[1:]

enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]
print(solution(enroll, referral, seller, amount))