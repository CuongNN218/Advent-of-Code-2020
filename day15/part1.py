starts = [15,12,0,14,3,1]
import time

check_dict = {}

for idx, start in enumerate(starts):
    check_dict[start] = [1, None ,idx]

turn = 6

start =time.time()
spoke_last = starts[turn - 1]
while turn < 30000000:        
    spoke_next = 0 if check_dict[spoke_last][0] == 1 else check_dict[spoke_last][2] - check_dict[spoke_last][1]
    if spoke_next  in check_dict:
        check_dict[spoke_next][0] += 1
        check_dict[spoke_next][1] = check_dict[spoke_next][2]
        check_dict[spoke_next][2] = turn
    else:
        check_dict[spoke_next] = [1, None, turn]
    spoke_last = spoke_next
    turn += 1
print(spoke_last)
print(time.time() - start)