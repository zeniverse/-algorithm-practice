
order = [4, 3, 1, 2, 5]

def solution(order):
    truck = []  # 트럭
    sub_belt = []   # 보조 벨트
    cur = 0 # 기사님이 주문한 택배 순서 번호
    idx = 1 # 현재 컨테이너 벨트에 있는 택배 번호

    while True:
        if cur == len(order):   # 택배를 트럭에 다 실음
            return len(order)
            
        if order[cur] == idx:   # 현재 컨테이너 벨트에서 바로 트럭에 실을 수 있음
            cur += 1    # 다음 택배 다루기
            idx += 1
            truck.append(idx)   # 택배 트럭에 싣기
        if order[cur] > idx:    # 컨테이너 벨트 저 너머에 택배가 있는 경우
            sub_belt += list(range(idx, order[cur]))   # 보조벨트에 택배를 실음
            idx = order[cur]    # 그 택배에 자리잡기
        elif order[cur] < idx:  # 보조 벨트에 택배가 있는 경우
            if sub_belt[-1] == order[cur]:  # 보조 벨트 끝의 택배라면
                cur += 1    # 보조 벨트에서 택배 꺼내서 싣기
                truck.append(idx)
                sub_belt.pop()
            else:   # 택배를 꺼낼 수 없다면
                return len(truck)

print(solution(order))