from collections import deque

def solution(cacheSize, cities):
    answer = 0
    queue = deque()

    for city in cities:
        city = city.lower()

        if city in queue:
            queue.remove(city)
            queue.append(city)
            answer += 1
        else:
            answer += 5
            queue.append(city)
            if len(queue) > cacheSize:
                queue.popleft()
                
    return answer

cacheSize = 0
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]

print(solution(cacheSize, cities))


