# Задача похожа первую только теперь нужно возвращать не кол-во максимумов, а сам максимум
# ну, и изменять по одному элементу
import math

n = int(input())
degree = 1
len_last_layer = 1
while len_last_layer < n:
    len_last_layer *= 2

segment_tree = (len_last_layer-1) * [-math.inf] + list(map(int, input().split())) + [-math.inf] * (len_last_layer-n)   # ДО (дерево отрезков)
promises = {}
for i in range(len(segment_tree)-len_last_layer-1, 0-1, -1):
    ind_child_l = i*2 + 1
    segment_tree[i] = max([segment_tree[ind_child_l], segment_tree[ind_child_l+1]]) # насчитываем для верхних слоев ДО

def get_max(end_l, end_r, now_l, now_r, now_ind):   # получаем максимум (почти как в первой задаче)
    if now_ind >= len(segment_tree) or end_l > now_r or end_r < now_l:
        return -math.inf
    if end_l <= now_l and end_r >= now_r:
        return segment_tree[now_ind]
    ind_child_l = now_ind*2 + 1
    max_left = get_max(end_l, end_r, now_l, (now_r+now_l)//2, ind_child_l)
    max_right = get_max(end_l, end_r, (now_r+now_l)//2 + 1, now_r, ind_child_l+1)
    return max([max_right, max_left])

# доходим до элемента через рекурсию и обнавляем его, потом возвращаем новый элемент и обнавляем предков
# сам код очень похож на получение максимума (обновление так же можно реализовать без рекурсии)
def update_segment_tree(num_el, new_el, now_l, now_r, now_ind):
    if now_ind >= len(segment_tree):
        return -math.inf
    if now_l > num_el or now_r < num_el: # не пересекает
        return segment_tree[now_ind]
    elif num_el == now_l and num_el == now_r:   # наш элемент
        segment_tree[now_ind] = new_el
        return new_el
    ind_child_l = now_ind*2 + 1
    max_left = update_segment_tree(num_el, new_el, now_l, (now_r + now_l) // 2, ind_child_l)
    max_right = update_segment_tree(num_el, new_el, (now_r + now_l) // 2 + 1, now_r, ind_child_l + 1)
    segment_tree[now_ind] = max([max_right, max_left])
    return max([max_right, max_left])

ans = []
for _ in range(int(input())):
    query = input().split()
    if query[0] == 's':
        ans.append(get_max(int(query[1]), int(query[2]), 1, len_last_layer, 0))
    else:
        update_segment_tree(int(query[1]), int(query[2]), 1,len_last_layer,0)

print(*ans)
