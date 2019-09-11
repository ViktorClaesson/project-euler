fib0 = 1
fib1 = 1
sum = 0
while fib0 < 4e6:
    if fib0 % 2 == 0:
        sum += fib0
    temp = fib0 + fib1
    fib0 = fib1
    fib1 = temp

print(sum)
