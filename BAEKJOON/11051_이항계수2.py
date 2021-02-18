# 이항계수2
n, k = map(int, input().split())
ans = 1

for i in range(2, n+1):
    ans *= i
for i in range(2, n-k+1):
    ans //= i
for i in range(2, k+1):
    ans //= i

print(ans % 10007)
