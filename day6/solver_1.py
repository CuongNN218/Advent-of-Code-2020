# read all groups in file

with open('input.txt', 'r') as file:
    contents = file.read()
groups = contents.split('\n\n')

for i in range(len(groups)):
    splited = groups[i].split('\n')
    groups[i] = splited

print(groups)

res = 0
for group in groups:
    ans_list = []
    for person in group:
        ans_list += person
    unique = set(ans_list)
    res += len(unique)

print(res)