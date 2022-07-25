
participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]	
dict = {}
sum = 0

for part in participant:
    dict[hash(part)] = part
    sum += hash(part)

for comp in completion:
    sum -= hash(comp)

print(dict[sum])



