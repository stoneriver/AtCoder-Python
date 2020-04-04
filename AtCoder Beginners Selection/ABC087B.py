# ABC087B - Coins


def scan500(X, A, B, C):
    X -= 500
    A -= 1
    if X < 0 or A < 0:
        return 0
    elif X == 0:
        return 1
    else:
        cnt = 0
        cnt += scan500(X, A, B, C)
        cnt += scan100(X, A, B, C)
        cnt += scan50(X, A, B, C)
        return cnt


def scan100(X, A, B, C):
    X -= 100
    B -= 1
    if X < 0 or B < 0:
        return 0
    elif X == 0:
        return 1
    else:
        cnt = 0
        cnt += scan100(X, A, B, C)
        cnt += scan50(X, A, B, C)
        return cnt
    

def scan50(X, A, B, C):
    X -= 50
    C -= 1
    if X < 0 or C < 0:
        return 0
    elif X == 0:
        return 1
    else:
        cnt = 0
        cnt += scan50(X, A, B, C)
        return cnt


A = int(input())
B = int(input())
C = int(input())
X = int(input())
cnt = 0
cnt += scan500(X, A, B, C)
cnt += scan100(X, A, B, C)
cnt += scan50(X, A, B, C)
print(cnt)

