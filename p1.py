def foo(n):
    if(n % 3 == 0 or n % 5 == 0):
        return n
    else:
        return 0


print(sum([foo(x) for x in range(1, 1000)]))
