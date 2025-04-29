n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
ans = [[0,0,0,0] for _ in range(n)] # храним ответ в двоичной системе (4 разряда)
for y in range(n):
    for x in range(n):
        num = matrix[y][x]
        two_in_degree = 1
        degree_now = 0
        while two_in_degree <= num:
            two_in_degree *= 2
            degree_now += 1
        two_in_degree //= 2
        degree_now -= 1

        count_one = 0
        while num > 0:
            if two_in_degree <= num:
                num -= two_in_degree
                count_one += 1
                ans[x][degree_now] = 1
                ans[y][degree_now] = 1
            two_in_degree //= 2
            degree_now -= 1
def from_binary_to_decimal(binary_num):
    two_in_degree = 1
    decimal_num = 0
    for digit in binary_num:
        decimal_num += two_in_degree if digit else 0
        two_in_degree *= 2
    return decimal_num

# print(*[from_binary_to_decimal(ans[i]) for i in range(n)])
print(*map(from_binary_to_decimal, ans))  # или так
