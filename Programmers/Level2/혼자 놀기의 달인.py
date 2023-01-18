
cards = [8,6,3,7,2,5,1,4]

def solution(cards):
    boxes = {idx + 1 : card for idx, card in enumerate(cards)}
    res = []

    while boxes:
        visited = set()
        position = list(boxes.keys())[0]

        while position not in visited:
            visited.add(position)
            tmp = boxes[position]
            del boxes[position]
            position = tmp
        res.append(len(visited))

    res.sort(reverse=True)

    return res[0] * res[1] if len(res) > 1 else 0

print(solution(cards))