n, k = map(int, input().split())
q = n // k
summ = k * (q * (q + 1)) // 2
print(summ)
