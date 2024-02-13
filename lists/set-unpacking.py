prep = set((1, 2, 3, 4, 5, 6, 3, 4, 5))

a, *b, d = prep # * b - unpacking in the middle 
print(a, *b, d)

# 1 2 3 4 5 6
