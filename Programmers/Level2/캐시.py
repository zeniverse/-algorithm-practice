
def solution(cacheSize, cities):
    cities = [c.upper() for c in cities]
    cache = []
    time = 0

    if cacheSize == 0:
        return len(cities) * 5
    else:
        for i in cities:
            if not i in cache:
                if len(cache) < cacheSize:
                    cache.append(i)
                    time += 5
                else:
                    cache.pop(0)
                    cache.append(i)
                    time += 5

            else:
                cache.pop(cache.index(i))
                cache.append(i)
                time += 1

    return time

cacheSize = 0
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]

print(solution(cacheSize, cities))


