
def solution(edges):
    answer = [0, 0, 0, 0]
    max_val = max(map(max, edges)) + 1
    in_arr, out_arr = [0] * max_val, [0] * max_val

    for o, i in edges:
        out_arr[o] += 1
        in_arr[i] += 1

    for now_node in range(1, max_val):
        if in_arr[now_node] == 0 and out_arr[now_node] >= 2:
            answer[0] = now_node
        elif in_arr[now_node] >= 1 and out_arr[now_node] == 0:
            answer[2] += 1
        elif in_arr[now_node] >= 2 and out_arr[now_node] == 2:
            answer[3] += 1
        
    answer[1] = out_arr[answer[0]] - sum(answer[2:])
    return answer

edges = [[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]
print(solution(edges))