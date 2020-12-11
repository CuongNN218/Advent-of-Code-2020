import os 

with open('input.txt', 'r') as input:
    nums = input.readlines()

# print(nums)
mapNum = {}
target = 2020

for i in range(len(nums)):
    nums[i] = int(nums[i].strip())

nums = sorted(nums)

array = sorted(nums)
check = set()
ans = []
for i in range(len(nums) - 2):
    left = i+1 
    right = len(nums) - 1
    while left < right:
        currentSum = array[i] + array[left] + array[right]
        if currentSum == target:
            combo = [array[i], array[left], array[right]]
            combo_t = tuple(combo)
            if combo_t not in check:
                ans.append([array[i], array[left], array[right]])
                check.add(combo_t)
            left += 1
            right -= 1
        elif currentSum < target:
            left += 1
        elif currentSum > target: 
            right -= 1
res = 1
for ele in ans[0]:
    res *= ele
print(res)