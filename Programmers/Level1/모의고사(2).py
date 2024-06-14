
answers = [1,3,2,4,2]

def solutions(answers):
    p = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    count = [0, 0, 0]

    for i, a in enumerate(answers):
        for j , b in enumerate(p):
            if a == b[i % len(b)]:
                count[i] += 1
    return [i + 1 for i, v in enumerate(count) if v == max(count)]

print(solutions(answers))


