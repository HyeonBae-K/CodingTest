matrix = []
for _ in range(8):
    matrix.append(list(map(str, list(input()))))

ans = 0
for i in range(8):
    for j in range(8):
        if (i+j) % 2 == 0:
            if matrix[i][j] == 'f' and 'F':
                ans += 1

print(ans)