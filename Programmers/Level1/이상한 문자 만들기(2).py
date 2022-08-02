s = "try hello world"

print(" ".join(map(lambda x : "".join([w.upper() if i % 2 == 0 else w.lower() for i, w in enumerate(x)]), s.split(" "))))