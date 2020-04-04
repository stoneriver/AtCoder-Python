# ABC086C - Traveling

N = int(input())
t, x, y = 0, 0, 0
possible = True

for i in range(N):
    ti, xi, yi = (int(j) for j in input().split())
    t = abs(ti - t)
    x = abs(xi - x)
    y = abs(yi - y)
    if x + y > t or (x + y - t) % 2 != 0:
        possible = False
        break

if possible:
    print("Yes")
else:
    print("No")
