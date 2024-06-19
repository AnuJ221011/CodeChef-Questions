t=int(input())
for _ in range(t):
    N,M=map(int, input().split())
    if N>M:
        print(N-M)
    else:
        mod=M%N
        print(min(N-mod,mod))