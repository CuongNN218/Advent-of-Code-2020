import fileinput 

lines = [l.strip() for l in fileinput.input('sample.txt')]

mask_vals = []

block = []

for line in lines:
    line = line.split('=')
    if 'mask' in line[0]:
        if len(block) > 0:
            mask_vals.append(block)
            block = []
        block.append(line[1].strip())
    elif 'mem' in line[0]:
        val_mem = int(line[0].split('[')[1][:-2])
        val = int(line[1].strip())
        block.append([val_mem, val])
mask_vals.append(block)
ans = 0

def convert2bin(val):
    str_bin = str(bin(val))[2:]
    str_bin = '0' * (36 - len(str_bin)) + str_bin
    return str_bin

def cal_res(mask, val):
    mask = mask[::-1]
    # print('mask:', mask)
    val = val[::-1]
    # print('val: ', val)
    res_str = ''
    for i in range(36):
        if mask[i] == 'X':
            res_str += val[i]
        elif mask[i] == '0':
            res_str += '0'
        elif mask[i] == '1':
            res_str += '1'
    # print('res: ', res_str)
    ans = 0
    for idx, bit in enumerate(res_str):
        # print('bit') 
        ans += int(bit) * (2 ** idx)
    return ans

ans_dict = {} 
for mask_val in mask_vals:
    # print(mask_val)
    mask = mask_val[0]
    for mem in mask_val[1:]:
        mem_id = mem[0]
        val = mem[1]
        ans_dict[mem_id] = cal_res(mask, convert2bin(val))

# print(ans_dict)
for key in ans_dict.keys():
    ans += ans_dict[key]

print(ans)
