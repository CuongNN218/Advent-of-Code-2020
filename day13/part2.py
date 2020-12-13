import fileinput
lines = list(fileinput.input('input.txt'))
ids = lines[1].strip().split(',')
# we can solve this problems using chinese remainder theorem

contrains = []
N = 1

# calculate inverse modulo
def mod_inverse(a, m): 
    m0 = m 
    y = 0
    x = 1
  
    if (m == 1): 
        return 0
  
    while (a > 1): 
  
        # q is quotient 
        q = a // m 
  
        t = m 
  
        # m is remainder now, process 
        # same as Euclid's algo 
        m = a % m 
        a = t 
        t = y 
  
        # Update x and y 
        y = x - q * y 
        x = t 
  
    # Make x positive 
    if (x < 0): 
        x = x + m0 
  
    return x 


# we need to solve the system of equations:
# x = b * k + i
# it mean that x ≡ (b - i) mod b for all B 
# so we need to establish the system of equation 1st:
for i, idx in enumerate(ids):
    if idx  != 'x':
        idx = int(idx)
        i %= idx
        contrains.append(((idx - i) % idx, idx)) 
        N *= idx

ans = 0

for i, idx in contrains:
    pi = int(N / idx)
    qi = int(mod_inverse(pi, idx))
    ans += int(i * pi * qi)

print(ans % N)