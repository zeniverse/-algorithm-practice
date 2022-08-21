record = ["Enter uid1234 Muzi",
"Enter uid4567 Prodo",
"Leave uid1234",
"Enter uid1234 Prodo",
"Change uid4567 Ryan"]

res = []
info_dict = {}
printer = {'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}

for rec in record:
    data = rec.split(" ")
    
    if data[0] != "Leave":
        info_dict[data[1]] = data[2]

print(info_dict)

for i in record:
    data = i.split(" ")

    if data[0] != 'Change':
        res.append(info_dict[data[1]] + printer[data[0]])

print(res)
