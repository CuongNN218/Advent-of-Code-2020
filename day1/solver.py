import os 

with open('input.txt', 'r') as input:
    nums = input.readlines()

# print(nums)
mapNum = {}
target = 2020

for i in range(len(nums)):
    nums[i] = int(nums[i].strip())
print(nums)
for i in range(len(nums)):
    if target - nums[i] in mapNum:
        print(target - nums[i], nums[i])
        result = (target - nums[i]) * nums[i]
        print(result)
    mapNum[nums[i]] = i

