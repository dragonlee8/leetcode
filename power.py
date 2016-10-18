def power(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    elif b == -1:
        return 1.0/a

    t1 = b/2
    t2 = b%2

    return power(a, t1) * power(a, t1) * power(a, t2)    

print power(2, -2)
print power(2, -4)
print power(2, -3)
print power(2, -9)
print power(2, -1)
