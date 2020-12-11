with open('input.txt', 'r') as file:
    lines = file.readlines()

seats = []
for line in lines:
    seats.append(line[:-1])

def row_int(row_s):
    left, right = 0, 127
    for char in row_s:
        mid = left + (right - left) // 2
        # print(char)
        # print(left, mid, right)
        if char == 'F':
            right = mid
        elif char == 'B':
            left = mid + 1
    return min(left, right)

def col_int(col_s):
    left, right = 0, 7
    for char in col_s:
        mid = left + (right - left) // 2
        # print(left, mid, right)
        if char == 'L':
            right = mid
        elif char == 'R':
            left = mid + 1
    return min(left, right)

def seat_id(row_int, col_int):
    return row_int * 8 + col_int

id_list = []

for seat in seats:
    row = row_int(seat[:7])
    col = col_int(seat[7:])
    id = seat_id(row, col)
    id_list.append(id)

for v in range(0,1024):
    if (v + 1) in id_list and (v - 1) in id_list and v not in id_list:
        print(v)

