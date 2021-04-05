n = int(input())
k = 0

for i in range(1 , 2*n):
    if i <= n:
        star = '*'*(2*i-1)
        space = ' '*(n-i)
        print(space + star + space)
    else:
        k += 1
        star = '*' * (2 * (i - (2*k)) - 1)
        space = ' ' * (n - (i-(2*k)))
        print(space + star + space)