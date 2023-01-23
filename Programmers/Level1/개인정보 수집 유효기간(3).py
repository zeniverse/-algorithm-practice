
today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

def to_days(date):
    year, month, day = map(int, date.split("."))
    return year * 12 * 28 + month * 28 + day

def solution(today, terms, privacies):
    months = {term[0]: int(term[2:]) * 28 for term in terms}
    today = to_days(today)
    res = [
        i + 1 for i, privacy in enumerate(privacies)
        if to_days(privacy[:-2]) + months[privacy[-1:]] <= today
    ]
    return res

print(solution(today, terms, privacies))