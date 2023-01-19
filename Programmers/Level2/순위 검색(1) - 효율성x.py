
info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

def solution(info, query):
    res = []

    for i in range(len(info)):
        info[i] = list(info[i].split(" "))
    
    for i in range(len(query)):
        q = list(query[i].split(" and "))
        q[3] = list(q[3].split(" "))
        count = 0
        for j in range(len(info)):
            if q[0] == info[j][0] or q[0] == "-":
                print(q[0], '0')
                if q[1] == info[j][1] or q[1] == "-":
                    print(q[1], '1')
                    if q[2] == info[j][2] or q[2] == "-":
                        print(q[2], '2')
                        if q[3][0] == info[j][3] or q[3][0] == "-":
                            print(q[3][0], '3-0')
                            if int(q[3][1]) <= int(info[j][4]):
                                print(q[3][1], '3-1')
                                count += 1
                                print(count)
        
        print('------')            
        res.append(count)


    return res

print(solution(info, query))