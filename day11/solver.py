import fileinput
# import re
from copy import deepcopy
p2 = 0
p1 = 0 
L = [list(l.strip()) for l in list(fileinput.input('input.txt'))]
# print(L)
R = len(L)
C = len(L[0])
print(R, C)
# print(L)

while True:
    newL = deepcopy(L)
    change = False
    for r in range(R):
        for c in range(C):
            nocc = 0
            for dr in [-1, 0 , 1]:
                for dc in [-1, 0, 1]:
                    # print(r, c)
                    if not (dr == 0 and dc == 0):
                        rr = r + dr
                        cc = c + dc
                        # print(rr, cc)
                        if 0 <= rr < R and 0 <= cc < C and L[rr][cc] == "#":
                            nocc +=1 
            # print(r, c, nocc)
            if L[r][c] == 'L':
                if nocc == 0:
                    newL[r][c] = '#'
                    change = True
            elif L[r][c] == '#' and nocc >= 4:
                newL[r][c] = 'L'
                change = True
    if not change:
        break
    L = deepcopy(newL)
                        
ans = 0
for r in range(R):
    for c in range(C):
        if L[r][c] == '#':
            ans += 1

print(ans)