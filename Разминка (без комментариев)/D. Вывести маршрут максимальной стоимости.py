n,m = list(map(int, input().split()))
matrix = [[-1]*(m+1)]
matrix[0][1] = 0
for y in range(1, n+1):
    matrix.append([-1] + list(map(int, input().split())))
    for x in range(1, m+1):
        matrix[y][x] += max(matrix[y][x-1], matrix[y-1][x])
x,y = -1,-1
path = []
for _ in range((m-1)+(n-1)):
    if matrix[y][x-1] > matrix[y-1][x]:
        path.append('R')
        x -= 1
    else:
        path.append('D')
        y -= 1
print(matrix[-1][-1])
print(' '.join(path[::-1]))