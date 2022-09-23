

cacheSize = 3
arr = [4, 2, 3, 4, 5, 6, 5, 4, 7]
cache = []

for i in arr:
    if not i in cache:
        if len(cache) < cacheSize:
            cache.append(i)
        else:
            cache.pop(0)
            cache.append(i)
    else:
        cache.pop(cache.index(i))
        cache.append(i)

print(cache)