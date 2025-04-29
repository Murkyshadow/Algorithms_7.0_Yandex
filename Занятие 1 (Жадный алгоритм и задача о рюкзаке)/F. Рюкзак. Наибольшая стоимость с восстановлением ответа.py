# как прошлая задача, только еще путь восстанавливаем
n, limit = map(int, input().split())
weights = list(map(int, input().split()))
costs = list(map(int, input().split()))
dp = []
for _ in range(n+1):
    dp.append([[-1,-1] for _ in range(limit+1)])

dp[0][0] = [0,-1]
for y in range(n):
    weight_item = weights[y]
    cost_item = costs[y]
    for x in range(limit, 0-1, -1):
        if dp[y][x][0] != -1:
            dp[y+1][x][0] = dp[y][x][0]
            dp[y+1][x][1] = dp[y][x][1]
            if x <= limit-weight_item and dp[y][x+weight_item][0] < dp[y][x][0]+cost_item:
                dp[y][x+weight_item][0] = dp[y][x][0] + cost_item
                dp[y][x+weight_item][1] = y
                dp[y+1][x + weight_item][0] = dp[y][x][0] + cost_item
                dp[y+1][x + weight_item][1] = y

dp.pop()
ind_best_cost = max(enumerate(dp[-1]), key=lambda x:x[1])[0]
now_ind_item = dp[-1][ind_best_cost][1]
min_ind_item = now_ind_item
ans = [now_ind_item+1]
while ind_best_cost > 0:
    weight = weights[now_ind_item]
    now_ind_item = dp[min_ind_item-1][ind_best_cost-weight][1]
    ind_best_cost -= weight
    ans.append(now_ind_item+1)
    min_ind_item = now_ind_item
print(*ans[-2::-1], sep='\n')

