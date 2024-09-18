def sayatAndSet(n, a):
    a = sorted(a)
    lrg = a[-1] - a[0]
    median = 0
    for i in range(n):
        if i == n//2:
            median = a[i]
    print(lrg, median)

n = int(input())
a = list(map(int, input().split()))
sayatAndSet(n, a)

