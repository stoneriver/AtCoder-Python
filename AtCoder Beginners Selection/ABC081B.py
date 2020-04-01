# ABC081B - Shift only

N = int(input())
A = [int(i) for i in input().split()]
cnt = -1
flg = True

while flg:
    cnt += 1
    for i in range(N):
        if A[i] % 2 == 0:
            A[i] /= 2
        else:
            flg = False
            break

print(cnt)