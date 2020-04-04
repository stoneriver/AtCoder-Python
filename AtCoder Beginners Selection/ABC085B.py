# ABC085B - Kagami Mochi

N = int(input())
d = [0 for i in range(N)]
for i in range(N):
    d[i] = int(input())
d.sort()
cnt = 1

for i in range(1, N):
    if d[i - 1] < d[i]:
        cnt += 1

print(cnt)
