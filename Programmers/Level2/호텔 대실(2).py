
def convert(time):
    h, m = time.split(":")
    return int(h) * 60 + int(m)

def solution(book_time):
    rooms = [0 for _ in range(24 * 60 + 10)]

    for i in book_time:
        checkIn = convert(i[0])
        checkOut = convert(i[1]) + 10

        rooms[checkIn] += 1
        rooms[checkOut] -= 1

    for i in range(1, len(rooms)):
        rooms[i] += rooms[i - 1]

    return max(rooms)


book_time = [["15:00", "17:00"], ["16:40", "18:20"],
             ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]
print(solution(book_time))