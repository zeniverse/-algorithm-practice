n = int(input())
count, sum_ = 0, 0
start, end = 0, 0

while end <= n:
    if sum_ < n:
        end += 1
        sum_ += end
    elif sum_ > n:
        sum_ -= start
        start += 1
    else:
        count += 1
        end += 1
        sum_ += end
print(count)