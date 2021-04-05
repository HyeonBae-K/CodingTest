import sys

#input = sys.stdin.readline()

m, n = map(int, input().split())
matrix = []
#행렬 입력
for i in range(m):
    matrix.append(list(map(int, input().split())))
#dp matrix 생성
dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
#dp : 2차원배열 , 각각 이전의 행과 열의 dp에 현재 행과 열의 값을 더하고 두번 더한 값은 뺀다.
for i in range(1, m+1):
    for j in range(1, n+1):
        dp[i][j] = matrix[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

k = int(input())
#(i,j) ~ (x,y) 값 = (x,y) dp 구하고 (i,j) dp를 뺀다. 두번 뺀 값은 한번 더한다.
for _ in range(k):
    i, j, y, x = map(int, input().split())
    ans = dp[y][x] - dp[y][j-1] - dp[i-1][x] + dp[i-1][j-1]
    print(ans)