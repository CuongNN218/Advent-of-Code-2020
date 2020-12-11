import fileinput
numbers = list([int(l) for l in fileinput.input(files='input.txt')])
print(numbers)

pre = 25
for index, number in enumerate(numbers[pre:]):
    # print(index)
    # print(number)
    pre_list = numbers[index:index+pre]
    print(pre_list)
    # print(len(pre_list))
    sum_list = set()
    for i in range(len(pre_list)):
        for j in range(i, len(pre_list)):
            sum = pre_list[i] + pre_list[j]
            sum_list.add(sum)
    print(sum_list)
    if number not in sum_list:
        print(number)
        break
    
