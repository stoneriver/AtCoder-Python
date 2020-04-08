# F - Division or Subtraction

# 愚直な実装で部分店もらう作戦

def gutyokunasousa(x, K):
    if x % K == 0:
        return x // K
    else:
        return x - K


N = int(input())
cnt = 0
for K in range(2, N + 1):
    if N % K == 1:
        cnt += 1
    elif N % K == 0:
        tmp = N
        while True:
            tmp = gutyokunasousa(tmp, K)
            if tmp % K == 1:
                cnt += 1
                break
            elif tmp % K == 0:
                continue
            else:
                break
print(cnt)