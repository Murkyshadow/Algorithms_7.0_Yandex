# для каждого цвета вычисляем все возможные длины комбинаций кирпичей (кроме комбинации со всеми кирпичами)
# далее берем 1ый цвет, выбираем длину и смотрим есть ли эта длина в остальных слоях,
# если если есть, то все хорошо YES, если нет, то переходим к след. длине, если
# проверили все длины, то выводим NO

def get_all_lenghts(bricks_one_color, max_len):
    dp_one_color = [-1]*(max_len+1)
    dp_one_color[0] = 0
    for num_brick in bricks_one_color:
        len_brick = bricks[num_brick]
        for i in range(max_len-len_brick, 0-1, -1):
            if dp_one_color[i] != -1 and dp_one_color[i+len_brick] == -1:
                dp_one_color[i + len_brick] = num_brick
    return dp_one_color

def get_path(lenghts, end_len):
    now_len = end_len
    path = []
    while now_len != 0:
        num_brick = lenghts[now_len]
        path.append(num_brick)
        now_len -= bricks[num_brick]
    return path

n, num_colors = map(int, input().split())
all_bricks_sort = {i:[] for i in range(1,101)}
bricks = [-1]
for num_brick in range(1, n+1):
    brick_l, brick_c = map(int, input().split())
    all_bricks_sort[brick_c].append(num_brick)
    bricks.append(brick_l)

dp = []
max_len = sum(bricks[i] for i in all_bricks_sort[1])
all_paths = []
for i in range(1, num_colors+1):
    dp.append(get_all_lenghts(all_bricks_sort[i], max_len))

ans = False
for now_len in range(1,max_len):
    flag_len = True
    for color in range(num_colors):
        if dp[color][now_len] == -1:
            flag_len = False
            break
    if flag_len:
        ans = now_len
        break

if ans:
    bricks_first_wall = []
    for c in range(num_colors):
        bricks_first_wall += get_path(dp[c], ans)
    print("YES")
    print(*bricks_first_wall)
else:
    print('NO')
