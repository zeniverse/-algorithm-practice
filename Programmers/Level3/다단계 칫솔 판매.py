
def solution(enroll, referral, seller, amount):
    graph = {}
    res = {e:0 for e in enroll}

    for e, r in zip(enroll, referral):
        graph[e] = r

    print(graph)

    for s, a in zip(seller, amount):
        money = a * 100
        rate = money // 10
        res[s] += money - rate
        x = graph[s]

        while x != "-":
            if rate == 0:
                break

            res[x] += rate - rate // 10
            rate //= 10
            x = graph[x]

    return list(res.values())

enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]
print(solution(enroll, referral, seller, amount))