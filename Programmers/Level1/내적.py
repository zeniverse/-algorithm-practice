a = [1,2,3,4]
b = [-3,-1,0,2]

res = 0

print(sum(aNum * bNum for aNum, bNum in zip(a, b)))
