import fileinput

L = [l.strip() for l in fileinput.input('input.txt')]
L.append('')
ON = set()

for r,l in enumerate(L):
    for c, ch in enumerate(l):
        if ch == '#':
            ON.add((r, c, 0, 0))
# print(ON)
for _ in range(6):
    NEW_ON = set()
    for x in range(-15, 15):
        for y in range(-15, 15):
            for z in range(-15, 15):
                for w in range(-15, 15):
                    nbr = 0 
                    for dx in [-1, 0, 1]:
                        for dy in [-1, 0 , 1]:
                            for dz in [-1, 0, 1]:
                                for dw in [-1, 0, 1]:
                                    if dx != 0 or dy != 0 or dz != 0 or dw != 0:
                                        if (x + dx, y + dy, z + dz, w + dw) in ON:
                                            nbr +=1
                    if (x, y, z, w) not in ON and nbr == 3:
                        NEW_ON.add((x, y, z, w))
                    if (x, y, z, w) in ON and nbr in [2, 3]:
                        NEW_ON.add((x, y, z, w))
    ON = NEW_ON


print(len(ON))