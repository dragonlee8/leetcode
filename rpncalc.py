def getLevel(s):
    if s == '+' or s=='-':
        return 2
    if s=='*' or s=='/':
        return 1
    return 0

def toRPN(s):
    if not s:
        return []

    num = None
    stack = []
    out = []
    for x in s:
        if x == ' ':
            if num:
                stack.append(num)
                num = None
            continue
        elif x.isdigit():
            if num:
                num = 10*num + int(x)
            else:
                num = int(x)
        elif x == '+' or x == '-' or x == '*' or x == '/':
            if num:
                stack.append(num)
                num = None
            signlevel = getLevel(x)
            while stack and stack[-1] != '(' and getLevel(stack[-1]) <= signlevel:
                out.append(stack[-1])
                stack.pop()

            stack.append(x)

        elif x == '(':
            if num:
                stack.append(num)
                num = None
            stack.append(x)
            continue
        elif x == ')':
            if num:
                stack.append(num)
                num = None
            while stack and stack[-1] != '(':
                out.append(stack[-1])
                stack.pop()
            stack.pop()

    if num:
        stack.append(num)
        num = None

    while stack:
        out.append(stack[-1])
        stack.pop()

    return out

def calc(num1, num2, op):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    else:
        return num1/num2

def eval(stack):
    if not stack:
        return 0

    tmp = []
    for x in stack:
        if x == '+' or x == '-' or x == '*' or x == '/':
            num2 = tmp.pop()
            num1 = tmp.pop()
            tmp.append(calc(num1, num2, x))
        else:
            tmp.append(x)

    return tmp[-1]

rpn = toRPN('1+2*4')
print eval(rpn)
