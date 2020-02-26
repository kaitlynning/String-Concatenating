x = [1, 2, 3, 4]

#use for and append
x1 = []
for item in x:
    x1.append([item, []])
print(x1)

#use list comprehension
print([[item, []] for item in x])

'''
[[1, []], [2, []], [3, []], [4, []]]
[[1, []], [2, []], [3, []], [4, []]]
'''