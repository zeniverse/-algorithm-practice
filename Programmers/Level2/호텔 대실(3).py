
# 누적합 사용 (이중 for문)

def solution(book_time):
    arr = [0 for _ in range(60 * 24)]

    for s, e in book_time:
        s_time = 60 * int(s[:2]) + int(s[3:])
        e_time = 60 * int(e[:2]) + int(e[3:])

        if e_time > 60 * 24 - 1:
            e_time = 60 * 24 - 1

        for i in range(s_time, e_time):
            arr[i] += 1

    return max(arr)


book_time = [["15:00", "17:00"], ["16:40", "18:20"],
             ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]
print(solution(book_time))