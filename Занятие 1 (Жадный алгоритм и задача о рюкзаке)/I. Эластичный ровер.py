# 21:31 22:54
# решается почти как F, только чтобы не выбирать наилучшее давленее сначала сортируем по давлению
# (чтобы не пришлось думать выдержит ли наша текщая комбинация предметов данное давление),
# и при добавлении нового предмета так же как в F выбираем наилучшую стоимость,
# но при этом идем до максимального объема + давления, которое выдерживает текущий предмет
import random

def new_sol_with_dict():
    n, limit = map(int, input().split())
    items = []
    max_v = 0
    for ind_item in range(n):
        v, c, p = map(int, input().split())
        items.append([v, c, p, ind_item])
        max_v += v

    sort_items = sorted(items, reverse=True, key=lambda x: x[2])
    dp = [{0:[0,-1]} for _ in range(n)]     # [best_cost, ind_item]

    indAfterSort_indBeforeSort = {}
    for num_item in range(n):
        volume_item = sort_items[num_item][0]
        cost_item = sort_items[num_item][1]
        pressure_item = sort_items[num_item][2]
        ind_item = sort_items[num_item][3]
        indAfterSort_indBeforeSort[num_item] = ind_item
        best_min = min([max_v, limit + pressure_item])
        new_items = []
        for now_v in dp[num_item]:
            if num_item != n-1:
                dp[num_item + 1][now_v] = [dp[num_item][now_v][0], dp[num_item][now_v][1]]

            new_cost = dp[num_item][now_v][0] + cost_item
            if now_v <= best_min - volume_item and (new_cost > dp[num_item].get(now_v + volume_item, [0])[0]):
                new_items.append([dp[num_item][now_v][0]+cost_item, num_item, now_v+volume_item])

        for data in new_items:
            dp[num_item][data[2]] = [data[0],data[1]]
            if num_item != n - 1:
                dp[num_item+1][data[2]] = [data[0], data[1]]

    ind_best_cost = max(dp[-1], key=lambda x: dp[-1][x][0])
    best_cost = dp[-1][ind_best_cost][0]
    now_ind_item = dp[-1][ind_best_cost][1]

    min_ind_item = now_ind_item
    path = []
    if now_ind_item != -1:
        path.append(indAfterSort_indBeforeSort[now_ind_item] + 1)
    while ind_best_cost > 0:
        volume = sort_items[now_ind_item][0]
        now_ind_item = dp[min_ind_item - 1][ind_best_cost-volume][1]
        ind_best_cost -= volume
        if now_ind_item == -1:
            break
        path.append(indAfterSort_indBeforeSort[now_ind_item] + 1)
        min_ind_item = min(min_ind_item, now_ind_item)

    print(len(path), best_cost)
    print(*path[::-1])

new_sol_with_dict()

# Тестики:
# 3 0
# 4 3 3
# 4 2 3
# 100 100 99
#
# 0 0

# 3 4
# 4 3 2
# 4 2 100
# 100 100 100

# 2 102
# 2 3

# 5 48
# 1 18 36
# 19 23 28
# 23 32 10
# 1 19 9
# 18 22 15

# ans 4, 92, [1, 2, 3, 4]