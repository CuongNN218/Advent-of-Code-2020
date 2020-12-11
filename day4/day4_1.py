with open('passport.txt', 'r') as file:
    lines = file.readlines()

# print(lines)

passports= []
id = []

count = 0
for line in lines:
    if line == '\n':
        passports.append(id)
        id = []
        # print(passports)
        # if count == 10:
        #     break
        count += 1
    else:
        id.append(line[:-1])
# print(id)
passports.append(id)

# fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']

count = 0
for passport in passports:
    #print(passport)
    pass_f = set()
    for element in passport:
        # print(element)
        element_list = element.split(' ')
        # print(element_list)
        # break
        for field in element_list:
            
            list_kv = field.split(':')
            
            key, value = list_kv[0], list_kv[1]
            print(key, value)
            pass_f.add(key)
    if len(pass_f) == 8 or (len(pass_f) == 7 and 'cid' not in pass_f) :
        count += 1
print(count)
