# динамичиски находим наибольшую стоимость, насчитывая для каждой массы наибольшую стоимость
# для этого к имеющимся массам (справо налево) добавляем текущую массу и выбираем наибольшую стоимость:
# текущая стоимость[now_ind] (в ячейках изначально -1)
# в ячейке или стоимость[now_ind-now_mass] + текущего предмета

import copy

n, limit = map(int, input().split())
weights = list(map(int, input().split()))
costs = list(map(int, input().split()))
dp = [[]]*n
dp[-1] = [[-1,-1] for _ in range(limit+1)]
dp[-1][0] = [0,-1]   # [best_cost, ind_item]
for y in range(n):
    dp[y] = copy.deepcopy(dp[y-1])
    weight_item = weights[y]
    cost_item = costs[y]
    for x in range(limit-weight_item, 0-1, -1):
        if dp[y][x][0] != -1 and dp[y][x+weight_item][0] < dp[y][x][0]+cost_item:
            dp[y][x + weight_item][0] = dp[y][x][0] + cost_item
            dp[y][x+weight_item][1] = y

ind_best_cost = max(enumerate(dp[-1]), key=lambda x:x[1])[0]
now_ind_item = dp[-1][ind_best_cost][1]
min_ind_item = now_ind_item
ans = [now_ind_item+1]
print(dp[-1][ind_best_cost][0])