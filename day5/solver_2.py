with open('input.txt', 'r') as file:
    lines = file.readlines()

seats = []
for line in lines:
    seats.append(line[:-1])

seats