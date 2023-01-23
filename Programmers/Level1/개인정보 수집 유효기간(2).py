
today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

def solution(today, terms, privacies):
    res = []
    term_dict = {}

    for term in terms:
        term = term.split(" ")
        term_dict[term[0]] = int(term[1]) * 28

    today = today.split(".")
    d = 12 * 28 * int(today[0]) + 28 * int(today[1]) + int(today[2])

    for i in range(len(privacies)):
        privacy = privacies[i].split(" ")   
        preDate = privacy[0].split(".")
        p = 12 * 28 * int(preDate[0]) + 28 * int(preDate[1]) + int(preDate[2])

        if p + term_dict[privacy[1]] <= d:
            res.append(i + 1)
    
    return res

print(solution(today, terms, privacies))