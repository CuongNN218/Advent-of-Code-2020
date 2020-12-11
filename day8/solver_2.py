import copy
with open('input.txt', 'r') as file:
    lines = file.readlines()

contents = []
for line in lines:
    line = line.split(' ')
    op_name = line[0]
    op, val = line[1][0], int(line[1][1:])
    contents.append([op_name, op, val])
full = len(contents)

def cal(contents):
    index = 0
    exe_cmds = [0]
    count = 0
    while True:
        current_index = index
        if index >= full:
            break
        if contents[index][0] in ['acc','nop']:
            index += 1         
        else:
            sign = 1 if contents[index][1] == '+' else -1
            index += sign * contents[index][2]
        if index < full:
            exe_cmds.append(index)
        count += 1
        if count == 10000:
            break
    return exe_cmds

fake_contents_list = []
for i, content in enumerate(contents):

    if content[0] == 'nop':
        fake_contents = copy.deepcopy(contents)
        fake_contents[i][0] = 'jmp'
        fake_contents_list.append(fake_contents)
        continue
    elif content[0] == 'jmp':
        fake_contents = copy.deepcopy(contents)
        fake_contents[i][0] = 'nop'
        fake_contents_list.append(fake_contents)
        continue
    else:
        continue
for j, fake_content in enumerate(fake_contents_list):
    cmds = cal(fake_content)
    if len(cmds) >= 10000:
        continue
    acc_cmds = cmds
    accumulate = 0
    for cmd in acc_cmds:
        if contents[cmd][0] == 'acc':
            sign = 1 if contents[cmd][1] == '+' else -1
            accumulate += sign * contents[cmd][2]
    print(acc_cmds)
    print(contents[7])
    print(fake_content[7])
    print(accumulate)


