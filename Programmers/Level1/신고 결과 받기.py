from collections import defaultdict

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]	
k = 2

def solution(id_list, report, k):
    report = list(set(report))
    answer = [0] * len(id_list)
    report_dic = defaultdict(list)
    count = defaultdict(int)
    
    for i in report:
        a, b = i.split()
        report_dic[a].append(b)
        count[b] += 1
        
    arr = []
    
    for n, c in count.items():
        if c >= k:
            arr.append(n)
            
    for i in range(len(id_list)):
        for j in arr:
            if j in report_dic[id_list[i]]:
                answer[i] += 1
    
    
    return answer

print(solution(id_list, report, k))