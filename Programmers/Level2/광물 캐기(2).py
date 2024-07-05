
def solution(picks, minerals):
    res = 0
    
    dic = {"diamond":0, "iron":0, "stone":0}
    pick = {0:(1, 1, 1), 1:(5, 1, 1), 2:(25, 5, 1)}

    arr = []
    length = min(sum(pick) * 5, len(minerals))

    for i in range(length):
        dic[minerals[i]] += 1

        # 5개씩 잘라서 나눔
        if (i + 1) % 5 == 0 or i == len(minerals) - 1:
            arr.append([dic["diamond"], dic["iron"], dic["stone"]])
            dic["diamond"], dic["iron"], dic["stone"] = 0, 0, 0 
    
    print(arr)

    arr.sort(key=lambda x: (x[0], x[1], x[2]), reverse=True)
    print(arr)

    for dia, iron, stone in arr:
        for i in range(3):
            if picks[i]:
                picks[i] -= 1
                res += (dia * pick[i][0]) + (iron * pick[i][1]) + (stone * pick[i][2])
                break

    return res

# 다이아, 철, 돌
picks = [1, 3, 2]
minerals = ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]
print(solution(picks, minerals))