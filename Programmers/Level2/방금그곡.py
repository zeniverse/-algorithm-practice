

m = "ABC"
musicinfos = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]

def change(s):
    s = s.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')
    return s

def solution(m, musicinfos):
    res = []
    m = change(m)

    for music in musicinfos:
        music = music.split(",")
        start = list(map(int, music[0].split(":")))
        end = list(map(int, music[1].split(":")))

        minute = ((end[0] * 60) + end[1]) -((start[0] * 60) + start[1])

        music[3] = change(music[3])
        sounds = music[3][:minute]

        while len(sounds) < minute:
            sounds += music[3][:minute]

        print(minute)
        print(sounds)
        if m in sounds:
            res.append((-minute, music[2]))

    if not res:
        return "(None)"
    else:
        return sorted(res)[0][1]

print(solution(m, musicinfos))