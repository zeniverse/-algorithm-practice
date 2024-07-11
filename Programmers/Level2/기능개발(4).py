
progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]

def solution(progresses, speeds):
    queue = []

    for p, s in zip(progresses, speeds):
        if not queue or queue[-1][0] < -((p-100)//s):
            queue.append([-((p-100) // s)])
        else:
            queue[-1][1] += 1

    return [q[1] for q in queue]