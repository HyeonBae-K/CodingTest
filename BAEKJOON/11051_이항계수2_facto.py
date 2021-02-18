# 이항계수2

def factorial(f):
    result = 1
    for i in range(2, f+1):
        result *= i
    return result


n, k = map(int, input().split())
a = factorial(n)
b = factorial(k)
z = factorial(n-k)

ans = a // b // z
print(ans % 10007)
