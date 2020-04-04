# ABC088B - Card Game for Two

N = int(input())
A = [int(i) for i in input().split()]
ptA, ptB = 0, 0
A.sort(reverse=True)

next = True  # Trueなら次にA、Falseなら次にBに追加
for n in A:
    if next:
        ptA += n
        next = False
    else:
        ptB += n
        next = True

print(abs(ptA - ptB))
