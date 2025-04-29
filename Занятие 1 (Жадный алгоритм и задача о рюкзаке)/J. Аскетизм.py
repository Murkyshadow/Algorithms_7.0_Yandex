import math
def Din_prog(days, mat_val_item, dp): # просчитываем все возможные комбинации материального, что бы понимать сколько материального мы можем вернуть и за сколько дней
    max_mat_val = 10000
    new_items = []
    for now_mat_val in dp:
        if max_mat_val - mat_val_item >= now_mat_val and dp.get(now_mat_val + mat_val_item, math.inf) > dp[now_mat_val]+days:
            new_items.append([now_mat_val + mat_val_item, dp[now_mat_val]+days])

    for ind, new_val in new_items:
        dp[ind] = new_val

def solution(n=None, limit=None, lines=None):
    n, limit = map(int, input().split())
    material_values = []
    for i in range(n):
        title, weight = input().split()
        material_values.append([title, int(weight)])

    sort_material_values = sorted(enumerate(material_values), key=lambda x:x[1][1])
    count_days_for_mat_val = {} # считаем сколько нужно дней для отказа от предмета
    max_mat_val = 0
    dp = {0:0}
    for ind, data in sort_material_values:
        title, mat_val_item = data
        refuse_max_mat_val = mat_val_item # не вернуть больше того от чего откажемся
        refuse_min_mat_val = mat_val_item - limit # но не можем отказать больше чем на дух. силу (чем вытерпит Вася)
        if refuse_min_mat_val <= 0: # можем отказаться без надобности что-то вернуть
            count_days_for_mat_val[ind] = 1
        elif max_mat_val < refuse_min_mat_val:  # если Вася не может вернуть столько материально сколько нужно для следущего отказа
            break
        else:
            best_days = math.inf
            for sum_mat_val in dp:
                if refuse_min_mat_val <= sum_mat_val and sum_mat_val <= refuse_max_mat_val and dp[sum_mat_val] < best_days:
                    best_days = dp[sum_mat_val]
            count_days_for_mat_val[ind] = best_days + 1
        Din_prog(count_days_for_mat_val[ind], mat_val_item, dp)
        max_mat_val += mat_val_item

    print(len(count_days_for_mat_val), sum(count_days_for_mat_val.values()))
    print(*sorted([material_values[ind][0] for ind in count_days_for_mat_val.keys()]), sep='\n')

solution()