from collections import defaultdict
            
def solution(tickets):
    dic = defaultdict(list)

    for i in tickets:
        dic[i[0]].append(i[1])
    for k, v in dic.items():
        v.sort(reverse=True)

    stack = ["ICN"]
    path = []

    while stack:
        top = stack[-1]

        if dic[top] != []:
            stack.append(dic[top].pop(0))
        else:
            path.append(stack.pop())

    return path[::-1]

tickets = [["ICN", "JFK"], ["ICN", "AAD"], ["JFK", "ICN"]]
print(solution(tickets))