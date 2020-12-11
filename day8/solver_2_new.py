import fileinput
import re
from copy import deepcopy

def run(P, ip, acc):
    words = P[ip]
    if words[0] == 'acc':
        acc += int(words[1])
        ip += 1
    elif words[0] == 'nop':
        ip += 1
    elif words[0] == 'jmp':
        ip += int(words[1])
    return (ip, acc)

P = list([l.split() for l in fileinput.input(files='test.txt')])

ip = 0
acc = 0
seen = []
list_inr = []
inr = []
while True:
    curr_ip = ip
    if ip in seen:
        print(acc)
        break
    seen.append(ip)
    ip, acc = run(P, ip, acc)
    if ip >= curr_ip:
        inr.append(curr_ip)
    else:
        inr.append(curr_ip)
        list_inr.append(inr)
        inr = []

Pmod = deepcopy(P)

if Pmod[list_inr[-2][-1]][0] == 'nop':
    Pmod[list_inr[-2][-1]][0] = 'jmp'
elif Pmod[list_inr[-2][-1]][0] == 'jmp':
    Pmod[list_inr[-2][-1]][0] = 'nop'

ip = 0
acc = 0
seen = []
while 0<=ip<len(Pmod):
    seen.append(ip)
    ip, acc = run(Pmod, ip, acc)
if ip == len(Pmod):
    print(acc)
