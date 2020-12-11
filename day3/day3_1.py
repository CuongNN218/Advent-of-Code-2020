dx = 1
dy = 2

res = 1
with open('tree.txt', 'r') as file:
    v = [x for x in file.read().split('\n')[::dy]]

trees = 0
x = 0
for y in v:    
    trees += (y[x % len(v[0])] == '#')
    x += dx

# print(trees)
