# ABC085C - Otoshidama
# 回帰なるからC++で提出したー
import sys


def scan10000(N, Y, x, y, z):
    N -= 1
    x += 1
    Y -= 10000
    if N == 0 and Y == 0:
        print(x, y, z)
        sys.exit(0)
    elif N > 0 and Y > 0:
        scan10000(N, Y, x, y, z)
        scan5000(N, Y, x, y, z)
        scan1000(N, Y, x, y, z)


def scan5000(N, Y, x, y, z):
    N -= 1
    y += 1
    Y -= 5000
    if N == 0 and Y == 0:
        print(x, y, z)
        sys.exit(0)
    elif N > 0 and Y > 0:
        scan5000(N, Y, x, y, z)
        scan1000(N, Y, x, y, z)


def scan1000(N, Y, x, y, z):
    N -= 1
    z += 1
    Y -= 1000
    if N == 0 and Y == 0:
        print(x, y, z)
        sys.exit(0)
    elif N > 0 and Y > 0:
        scan1000(N, Y, x, y, z)


N, Y = (int(i) for i in input().split())
scan10000(N, Y, 0, 0, 0)
scan5000(N, Y, 0, 0, 0)
scan1000(N, Y, 0, 0, 0)
print(-1, -1, -1)
