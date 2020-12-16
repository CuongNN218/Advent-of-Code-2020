import fileinput

block = []
blocks = []
for line in fileinput.input('input.txt'):
    if line == '\n':
        blocks.append(block)
        block = []
    else:
        block.append(line[:-1])
blocks.append(block)
print(blocks)

ans = []

ranges = []
for field in blocks[0]:
    splited = field.split(' ')
    range_1, range_2 = splited[-3].split('-'), splited[-1].split('-')
    print(range_1, range_2)
    range_1 = range(int(range_1[0]), int(range_1[1]) + 1)
    range_2 = range(int(range_2[0]), int(range_2[1]) + 1)
    ranges.append(range_1)
    ranges.append(range_2)
print(ranges)    

all_seats = []
print(blocks[-1])
for seat_line in blocks[-1][1:]:
    seats = seat_line.split(',')
    for seat in seats:
        seat = int(seat)
        check = False
        for range in ranges:
            if seat in range:
                check = True
        if check == False:
            all_seats.append(seat)
print(sum(all_seats))
