def is_pal(n):
    for a, b in zip(str(n), str(n)[::-1]):
        if(a != b):
            return False
    return True


pals = []
for x in range(999, 99, -1):
    for y in range(x, 99, -1):
        if(is_pal(x * y)):
            pals.append(x * y)

print('max:', max(pals))
