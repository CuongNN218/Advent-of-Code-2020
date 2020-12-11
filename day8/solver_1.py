with open('input.txt', 'r') as file:
    lines = file.readlines()

contents = []
for line in lines:
    line = line.split(' ')
    op_name = line[0]
    op, val = line[1][0], int(line[1][1:])
    contents.append([op_name, op, val])

exe_cmds = [0]
index = 0

while True:
    if contents[index][0] in ['acc','nop']:
        index += 1         
    else:
        sign = 1 if contents[index][1] == '+' else -1
        index += sign * contents[index][2]
    if index not in exe_cmds:
        exe_cmds.append(index)
    else:
        accumulate = 0
        for cmd in exe_cmds:
            if contents[cmd][0] == 'acc':
                sign = 1 if contents[cmd][1] == '+' else -1
                accumulate += sign * contents[cmd][2]
        print(accumulate)
        break
