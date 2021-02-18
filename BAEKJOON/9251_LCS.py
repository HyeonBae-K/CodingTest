# LCS
s1 = list(str(input()))
s2 = list(str(input()))
s1_len = len(s1)
s2_len = len(s2)
matrix = [[0]*(s1_len+1)for _ in range(s2_len + 1)]

for i in range(1, s1_len+1):
    for j in range(1, s2_len+1):
        if s1[i-1] == s2[j-1]:
            matrix[i][j] = matrix[i-1][j-1]+1
        else:
            matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])

print(matrix[-1][-1])
