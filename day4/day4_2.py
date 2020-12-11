
with open('passport.txt', 'r') as file:
    lines = file.readlines()

# print(lines)

passports= []
id = []

for line in lines:
    if line == '\n':
        passports.append(id)
        id = []
    else:
        id.append(line[:-1])
# print(id)
passports.append(id)

count_all = 0
count_false = 0
ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
hcl = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a' , 'b', 'c', 'd', 'e', 'f']
for passport in passports:
    # print(passport)
    
    pass_f = dict()
    for element in passport:
        # print(element)
        element_list = element.split(' ')
        for field in element_list:
            list_kv = field.split(':')
            key, value = list_kv[0], list_kv[1]
            # print(key, value)
            if key == 'byr': # 4 so  1919 < < 2002
                if len(value) == 4:
                    pass_f[key] = 1 if int(value) < 2003 and int(value) > 1919 else 0  
                else:
                    pass_f[key] = 0
            if key == 'iyr': # 4 so 2009 < < 2020
                if len(value) == 4:
                    pass_f[key] = 1 if int(value) < 2021 and int(value) > 2008 else 0
                else:
                    pass_f[key] = 0 
            if key == 'eyr': # 4 so 2009 < < 2020
                if len(value) == 4:
                    pass_f[key] = 1 if int(value) < 2021 and int(value) > 2008 else 0
                else:
                    pass_f[key] = 0
            if key == 'hgt': # cm: 150 - 193 in 59 76
                if value[-2:] == 'cm':
                    pass_f[key] = 1 if int(value[:-2]) > 149 and int(value[:-2]) < 194 else 0
                elif value[-2:] == 'in':
                    pass_f[key] = 1 if int(value[:-2]) > 58 and int(value[:-2]) < 76 else 0
                else:
                    pass_f[key] = 0
            if key == 'hcl': # 0-9 a-f
                if value[0] == '#':
                    for char in value[1:]:
                        
                        if char in hcl:
                            pass_f[key] = 1
                        else:
                            pass_f[key] = 0
                            break
                else:
                    pass_f[key] = 0
            if key == 'ecl':
                pass_f[key] = 1 if value in ecl else 0
            if key == 'pid': # 9 so toan la so
                pass_f[key] = 1 if any(char.isdigit() for char in value) else 0
            if key == 'cid': # co cung duoc deo co khong sao
                pass_f[key] = 1  

    if len(pass_f.keys()) == 8 or (len(pass_f.keys()) == 7 and 'cid' not in pass_f) :
        count_all += 1
        # print(pass_f)
        for key, value_k in pass_f.items():
            if value_k == 0 and key != 'cid':
                count_false += 1
                print(passport)
                print("INVALID")
                break
        
        # if check_sum == 8:
        #     count += 1
        #     print(pass_f)
        #     print('VALID')
        # elif check_sum == 7 and 'cid' not in pass_f.keys():
        #     count += 1
        #     print(pass_f)
        #     print('VALID')
        # else:
        #     print('INVALID')
        # break
    #         count += 1
print(count_all)
print(count_false)