
def change(time):
    h, m = map(int, time.split(":"))
    return h * 60 + m

def check_op(pos, op_start, op_end):
    if op_start <= pos and pos <= op_end:
        pos = op_end
    return pos

def solution(video_len, pos, op_start, op_end, commands):
    video_len = change(video_len)
    pos = change(pos)
    op_start = change(op_start)
    op_end = change(op_end)

    pos = check_op(pos, op_start, op_end)

    for c in commands:
        if c == "next":
            pos = min(video_len, pos + 10)
        else:
            pos = max(0, pos - 10)

        pos = check_op(pos, op_start, op_end)

    h = str(pos // 60).zfill(2)
    m = str(pos % 60).zfill(2)

    return h + ":" + m

video_len, pos, op_start, op_end, commands = "10:55", "00:05", "00:15", "06:55", ["prev", "next", "next"]

print(solution(video_len, pos, op_start, op_end, commands))

