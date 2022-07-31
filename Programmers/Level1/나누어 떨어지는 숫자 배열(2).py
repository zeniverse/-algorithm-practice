arr = [3,2,6]
divisor = 10

print(sorted([i for i in arr if i % 10 == 0]) or [-1])

## 앞의 조건이 False일때 or 뒤의 리스트가가 출력된다