# read all groups in file

with open('input.txt', 'r') as file:
    contents = file.read()
groups = contents.split('\n\n')

for i in range(len(groups)):
    splited = groups[i].split('\n')
    groups[i] = splited

question_name = ''
res = 0
for group in groups:
    ans_list = []
    print(group)
    if len(group) == 1:
        res += len(group[0])
    else:
        n_person = len(group)
        dict_freq = {}
        for person in group:
            for char in person:
                dict_freq[char] = dict_freq.get(char, 0) + 1
        for element in dict_freq.keys():
            res += 1 if dict_freq[element] == n_person else 0

print(res)
             


            
        




        
            
    

print(res)