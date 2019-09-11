from math import ceil

N = 600851475143
n = ceil(N**.5)
divs = []
curr = 2

while(curr < n):
    if N % curr == 0:
        divs.append(curr)
        N = N / curr
        n = ceil(N**.5)
        curr = 2
    else:
        curr += 1
divs.append(int(N))

print(divs)
print('max:', max(divs))
