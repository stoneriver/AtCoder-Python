# B - Popular Vote

N, M = (int(i) for i in input().split())
A = [int(i) for i in input().split()]
A.sort(reverse=True)
V = 0

for a in A:
    V += a

if A[M - 1] < V / (4 * M):
    print("No")
else:
    print("Yes")
