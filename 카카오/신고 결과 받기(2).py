
id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

res = [0] * len(id_list)
report_dict = {x : 0 for x in id_list}

for i in report:
    report_dict[i.split()[1]] += 1

for i in report:
    if report_dict[i.split()[1]] >= k:
        res[id_list.index(i.split()[0])] += 1

print(res)