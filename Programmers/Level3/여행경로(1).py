from collections import defaultdict
            
def solution(tickets):
    dic = defaultdict(list)
    path = []

    for i in tickets:
        dic[i[0]].append(i[1])
    for k, v in dic.items():
        v.sort(reverse=True)

    stack = ["ICN"]

    while stack:
        top = stack.pop()

        if top not in dic or not dic[top]:
            path.append(top)
        else:
            stack.append(top)
            stack.append(dic[top].pop())

    return path[::-1]

tickets = [["ICN", "JFK"], ["ICN", "AAD"], ["JFK", "ICN"]]
print(solution(tickets))