import fileinput 

lines = [l.strip() for l in fileinput.input('input.txt')]

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
    val = val[::-1]
    res_str = ''
    count = 0
    for i in range(36):
        if mask[i] == '0':
            res_str += val[i]
        elif mask[i] == 'X':
            count += 1
            res_str += 'X'
        elif mask[i] == '1':
            res_str += '1'
    return res_str, count

def convert2dec(res_str):
    ans = 0
    for idx, bit in enumerate(res_str):
        ans += int(bit) * (2 ** idx)
    return ans 

def gen_all_mem(res_str, nums):
    all_str = [res_str]
    while True:
        str = all_str.pop(0)
        to_list = list(str)
        for i, char in enumerate(to_list):
            if char == 'X':
                to_list[i] = '1'
                all_str.append(''.join(to_list))
                to_list[i] = '0'
                all_str.append(''.join(to_list))
                break
        if len(all_str) == (2 ** nums): 
            break      
    ans = []      
    for str in all_str:
        ans.append(convert2dec(str))
    return ans 

ans_dict = {} 
for mask_val in mask_vals:
    # print(mask_val)
    mask = mask_val[0]
    for mem in mask_val[1:]:
        mem_id = mem[0]
        val = mem[1]

        res_str, nums = cal_res(mask, convert2bin(mem_id))
        list_ans = gen_all_mem(res_str, nums)

        for ele in list_ans:
            ans_dict[ele] = val

for key in ans_dict.keys():
    ans += ans_dict[key]

print(ans)