# ABC083B - Some Sums


N, A, B = (int(i) for i in input().split())
S = 0

for n in range(N+1):
    sum = 0
    nctrl = n
    while nctrl != 0:
        sum += nctrl % 10
        nctrl //= 10
    if A <= sum and sum <= B:
        S += n

print(S)