absolutes = [4,7,12]
signs = [True,False,True]

print(sum(absolute if sign else -absolute for absolute, sign in zip(absolutes, signs)))

