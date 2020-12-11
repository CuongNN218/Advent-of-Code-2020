with open('input.txt', 'r') as input:
    lines = input.readlines()
print(len(lines))
count = 0

for line in lines:
    lineList = line.strip().split(' ')
    
    range_r = lineList[0].split('-')
    char = lineList[1][:-1]
    min_p = int(range_r[0])
    max_p = int(range_r[1])
    string = list(lineList[-1])
    count_r = 0
    if string[min_p - 1] == char:
        count_r += 1
    if string[max_p - 1] == char:
        count_r += 1
    if count_r == 1:
        count += 1
        print(string, max_p, min_p, char)

print(count)
    

    

