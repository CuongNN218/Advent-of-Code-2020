import fileinput

l = [l.strip() for l in fileinput.input('tung_input.txt')]

ids = l[1].split(',')

filtered = []

for id in ids:
    if id != 'x':
        filtered.append(int(id))
time_stamp = int(l[0])

time_stamps = []

for id in filtered:
    mul = time_stamp // id
    time_stamps.append(mul * id)
    time_stamps.append((mul + 1) * id)

min_t = 1000000
res = 0

for tmp in time_stamps:
    if abs(tmp - time_stamp) <= min_t and tmp > time_stamp:
        min_t = tmp - time_stamp
        res = tmp
co_id = 0
for id in filtered:
    if res % id == 0:
        co_id = id

print((res - time_stamp) * co_id)


