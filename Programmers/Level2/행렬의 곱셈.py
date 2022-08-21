arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]

print([[sum(a * b for a, b in zip(arr1_row, arr2_col)) for arr2_col in zip(*arr2)] for arr1_row in arr1])
