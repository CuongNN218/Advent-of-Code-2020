import fileinput
from itertools import accumulate 

numbers = list([int(l) for l in fileinput.input(files='input.txt')])
print(numbers)

pre = 25
invalid =0
invalid_index = 0

def twoSum(nums, target):
    dict_nums = {}
    for i in range(len(nums)):
        comp = target - nums[i]
        if comp in dict_nums:
            return True
        dict_nums[nums[i]] = i
    return False

for index, number in enumerate(numbers[pre:]):
    pre_list = numbers[index:index+pre]
    if not twoSum(pre_list, number):
        invalid = number
        invalid_index = index + pre
        break
print(invalid, invalid_index)
def cumulativeSum(input): 
    return list(accumulate(input))

prefix_sum = cumulativeSum(numbers[:invalid_index])

dict_nums = {}
for i in range(len(prefix_sum)):
    comp = - invalid + prefix_sum[i]
    if comp in dict_nums:
        sub_list = numbers[dict_nums[comp] + 1: i + 1]
        print(max(sub_list) +  min(sub_list))
        break
    dict_nums[prefix_sum[i]] = i




