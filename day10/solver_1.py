import fileinput
numbers = list([int(l) for l in fileinput.input(files='input.txt')])
print(numbers)

jolt_1 = 1
jolt_3 = 3

count_1 = 0
count_3 = 0

start = 0
end = max(numbers)
print(end)
t = 0
while start <= end and t < len(numbers):
    current = 0
    print(list(range(start, start + 4)))
    for jolt in range(start + 1, start + 4):
        if jolt in numbers:
            current = jolt
            break

    if current - start == 1:
        count_1 += 1
    elif current - start == 3:
        count_3 += 1
    start = current
    t += 1

print(count_1 * (count_3 + 1))