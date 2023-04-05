def convert_minutes(minute):
    HH = str(minute // 60)
    MM = str(minute % 60)

    if len(HH) == 1:
        HH = '0' + HH
    if len(MM) == 1:
        MM = '0' + MM
    
    return HH+":"+MM

def solution(n, t, m, timetable):
    tmp = []
    for s in timetable:
        HH = s[:2]
        MM = s[3:]
        tmp.append(int(HH) * 60 + int(MM))
    tmp.sort()
    timetable = tmp

    shuttles = [[] for _ in range(n)]
    departure_time = [540 + (i * t) for i in range(n)]

    idx_person = 0               # 다음에 탑승할 사람 index
    for i, shuttle in enumerate(shuttles):
        dt = departure_time[i]   # 셔틀 출발 시간
        cnt_onboard = 0          # 셔틀에 탄 사람 수 

        while cnt_onboard < m and (idx_person < len(timetable) and dt >= timetable[idx_person]):
            shuttle.append(idx_person)
            idx_person += 1
            cnt_onboard += 1

    # 마지막 셔틀에 자리가 남는 경우
    if len(shuttles[-1]) < m:
        return convert_minutes(departure_time[-1])
    
    # 마지막 셔틀에 자리가 꽉찬 경우
    return convert_minutes(timetable[shuttles[-1][-1]] - 1)


n, t, m = 1, 1, 5
timetable = ["08:00", "08:01", "08:02", "08:03"]
print(solution(n, t, m, timetable))