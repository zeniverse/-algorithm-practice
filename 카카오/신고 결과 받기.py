from collections import defaultdict

id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 2
res = []
report_user = []

report_dict = defaultdict(list)
count_dict = defaultdict(int)

report = list(set(report))

for i in report:
    a, b = i.split()
    report_dict[a].append(b)
    count_dict[b] += 1

    if count_dict[b] >= k:
        report_user.append(b)

for user in id_list:
    tmp = report_dict[user]
    res.append(len(list(set(tmp).intersection(report_user))))

print(res)