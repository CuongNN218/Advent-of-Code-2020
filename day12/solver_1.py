import fileinput

lines = [l.strip() for l in fileinput.input('input.txt')]

dx = [1, 0, -1, 0] 
dy = [0, -1, 0, 1] # anti clock-wise

x = 0
y = 0
ang = 0
for line in lines:
    cmd = line[0]
    val = int(line[1:])
    if cmd == 'N':
        y += val
    elif cmd == 'S':
        y -= val
    elif cmd == 'E':
        x += val
    elif cmd == 'W':
        x -= val
    elif cmd == 'L':
        ang = ang + 3 * val
    elif cmd == 'R': 
        ang = ang + val
    elif cmd == 'F':
        print(ang)
        x += val * dx[((ang) // 90) % 4]
        y += val * dy[((ang) // 90) % 4]
    print(x, y)

print(abs(x) + abs(y))
