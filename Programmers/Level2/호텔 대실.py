import heapq

def convert(time):
    h, m = time.split(":")
    return int(h) * 60 + int(m)

def solution(book_time):
    res = 1
    book_times = sorted([[convert(time[0]), convert(time[1])] for time in book_time])

    queue = []

    for start, end in book_times:
        if not queue:
            heapq.heappush(queue, end)
            continue
        
        if queue[0] <= start:
            heapq.heappop(queue)
        else:
            res += 1
        
        heapq.heappush(queue, end + 10)

    return res


book_time = [["15:00", "17:00"], ["16:40", "18:20"],
             ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]
print(solution(book_time))