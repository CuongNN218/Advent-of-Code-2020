import fileinput
L = [l.strip() for l in fileinput.input('input.txt')]
def precedence(op):
    if op == '+':
        return 2
    elif op == '*':
        return 1
    return 0
 
def applyOp(a, b, op):
     
    if op == '+': return a + b
    if op == '*': return a * b
 
def evaluate(tokens):
     

    values = []
    ops = []
    i = 0
     
    while i < len(tokens):
         
        if tokens[i] == ' ':
            i += 1
            continue
         
        # Current token is an opening 
        # brace, push it to 'ops'
        elif tokens[i] == '(':
            ops.append(tokens[i])
         
        # Current token is a number, push 
        # it to stack for numbers.
        elif tokens[i].isdigit():
            val = 0
            while (i < len(tokens) and
                tokens[i].isdigit()):
             
                val = (val * 10) + int(tokens[i])
                i += 1
            values.append(val)
            i-=1
         

        elif tokens[i] == ')':
         
            while len(ops) != 0 and ops[-1] != '(':
             
                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()
                 
                values.append(applyOp(val1, val2, op))
             
            # pop opening brace.
            ops.pop()
         
        # Current token is an operator.
        else:

            while (len(ops) != 0 and
                precedence(ops[-1]) >=
                   precedence(tokens[i])):
                         
                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()
                 
                values.append(applyOp(val1, val2, op))
             
            # Push current token to 'ops'.
            ops.append(tokens[i])
         
        i += 1
    
    while len(ops) != 0:
         
        val2 = values.pop()
        val1 = values.pop()
        op = ops.pop()
                 
        values.append(applyOp(val1, val2, op))
    
    return values[-1]

ans = 0
for l in L:
    ans += evaluate(l)
print(ans) 

