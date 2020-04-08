# C - Replacing Integer

N, K = (int(i) for i in input().split())
N -= (N // K) * K
print(min(N, abs(N - K)))
