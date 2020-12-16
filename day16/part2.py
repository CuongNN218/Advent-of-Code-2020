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
# print(blocks)

ans = []

ranges = []

for field in blocks[0]:
    splited = field.split(' ')
    range_1, range_2 = splited[-3].split('-'), splited[-1].split('-')
    # print(range_1, range_2)

    range_1 = range(int(range_1[0]), int(range_1[1]) + 1)
    range_2 = range(int(range_2[0]), int(range_2[1]) + 1)
    ranges.append(range_1)
    ranges.append(range_2)

all_seats = []
invalid_tickets = []

for seat_line in blocks[-1][1:]:
    seats = seat_line.split(',')
    int_seats = [int(seat) for seat in seats]
    for idx, seat in enumerate(seats):
        seat = int(seat)
        check = False
        for range_check in ranges:
            if seat in range_check:
                check = True
        if check == False:
            invalid_tickets.append(int_seats)
    all_seats.append(int_seats)

valid_ticket = []
for ticket in all_seats:
    if ticket not in invalid_tickets:
        valid_ticket.append(ticket)
valid_ticket.append([139,109,61,149,101,89,103,53,107,59,73,151,71,67,97,113,83,163,137,167])
# for col in valid_ticket:
import numpy as np
matrix = np.array(valid_ticket)
print(matrix.shape)

idxss = []
cols = []
for k in range(20): 
    for i in range(20):
        if i not in cols:
            col = matrix[:, i]
            idxs = []
            for idx in range(0, len(ranges), 2):
                if idx not in idxs:
                    n = 191
                    check = n
                    range_1, range_2 = ranges[idx], ranges[idx + 1]
                    for ele in col:
                        if ele not in range_1 and ele not in range_2:
                            check -= 1
                    if check == 191 and idx // 2 not in idxss:
                        idxs.append(idx // 2)
            if len(idxs) == 1:
                idxss.append(idxs[0])
                cols.append(i)

vals = [139,109,61,149,101,89,103,53,107,59,73,151,71,67,97,113,83,163,137,167]
ans = 1
for col, con in zip(cols, idxss):
    if con < 6:
        ans *= vals[col]
print(ans)


