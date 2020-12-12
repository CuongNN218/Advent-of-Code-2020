import fileinput
lines = [l.strip() for l in fileinput.input('input.txt')]

x = 0
y = 0
wpx, wpy = 10, 1

for line in lines:
    cmd = line[0]
    val = int(line[1:])
    if cmd == 'N':
        wpy += val
    elif cmd == 'S':
        wpy -= val
    elif cmd == 'E':
        wpx += val
    elif cmd == 'W':
        wpx -= val
    elif cmd == 'L':
        for _ in range(val // 90):
            wpx, wpy = -wpy, wpx
    elif cmd == 'R': 
        for _ in range(val// 90):
            wpx, wpy = wpy, -wpx
    elif cmd == 'F':
        x += val * wpx
        y += val * wpy
print(abs(x) + abs(y))
