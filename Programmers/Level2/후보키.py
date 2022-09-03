

from itertools import combinations


relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]

def solution(relation):
    row = len(relation)
    col = len(relation[0])

    # 전체 조합
    combi = []
    for i in range(1, col + 1):
        combi.extend(combinations(range(col), i))

    print(combi)

    # 유일성
    unique = []
    for c in combi:
        tmp = [tuple(item[i] for i in c) for item in relation]
        print(tmp)

        if len(set(tmp)) == row:
            put = True

            for x in unique:
                if set(x).issubset(set(c)): # 최소성
                    print('###########', set(x)&(set(c)))
                    put = False
                    break

            if put:
                print('******', c)
                unique.append(c)

    return len(unique)


print(solution(relation))