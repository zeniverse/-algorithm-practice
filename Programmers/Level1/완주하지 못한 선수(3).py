import collections

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]	

res = collections.Counter(participant) - collections.Counter(completion)

print(collections.Counter(participant))
print(collections.Counter(completion))

print(list(res)[0])


