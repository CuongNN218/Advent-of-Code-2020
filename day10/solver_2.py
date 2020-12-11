import fileinput
numbers = list([int(l) for l in fileinput.input(files='test_2.txt')])
# nums
max_path = [0] + sorted(numbers) + [max(numbers)+3]
dp = [0] * len(max_path) 

dp[0] = 1
dp[1] = 1
dp[2] = 2

for i in range(3, len(max_path)): 
    check_list = [*range(max_path[i] - 1 , max_path[i] - 4, -1)]
    dp[i] += dp[i - 1] if max_path[i - 1] in check_list else 0
    dp[i] += dp[i - 2] if max_path[i - 2] in check_list else 0
    dp[i] += dp[i - 3] if max_path[i - 3] in check_list else 0
    print(i, dp[i])

# print(dp)