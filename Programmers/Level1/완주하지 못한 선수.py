
participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]	
res = ''

participant.sort()
completion.sort()


for i in range(len(completion)):
    if(participant[i] != completion[i]):
        res = participant[i]
        break

if res == '':
    res = participant[-1]

print(res)




