# так же решаем через ДО, в узлах храним максимум на отрезке

n, m = map(int,input().split())
for i in range(1000000):
    if 2**i >= n:
        break
len_last_layer = 2**i
segment_tree = (len_last_layer-1)*[None] + list(map(int, input().split())) + [-1] * (len_last_layer-n)
for i in range(len_last_layer-2, 0-1, -1):
    left_child = i*2 + 1
    segment_tree[i] = max([segment_tree[left_child], segment_tree[left_child+1]])

def search(left, x, now_l, now_r, ind_now): # ищем число >= x, которое не левее данного индекса
    if ind_now >= len(segment_tree) or now_r < left or segment_tree[ind_now] < x:   # если левее или число <x
        return -1
    elif now_l == now_r:    # дошли до числа - вернули ответ
        return now_l
    left_child = ind_now*2 + 1
    res_l = search(left,x,now_l,(now_l+now_r)//2, left_child)   # ищем в левом ребенке
    if res_l != -1: # если в левом нашли, то сразу возвращаем ответ
        return res_l
    return search(left,x,(now_l+now_r)//2+1, now_r, left_child+1)   # иначе возвращаем ответ из правого

def update_el(num_new_el, new_el, now_l, now_r, now_ind):   # обновление почти такое же как в прошлом решении
    if now_ind >= len(segment_tree) or now_l > num_new_el or now_r < num_new_el:
        return segment_tree[now_ind]
    if now_l == now_r and now_l == num_new_el:
        segment_tree[now_ind] = new_el
        return new_el
    left_child = now_ind*2 + 1
    l_max = update_el(num_new_el, new_el, now_l, (now_l+now_r)//2, left_child)
    r_max = update_el(num_new_el, new_el, (now_l + now_r)//2+1, now_r, left_child+1)
    segment_tree[now_ind] = max([l_max, r_max])
    return segment_tree[now_ind]

ans = []
for _ in range(m):
    type, ind, x = map(int, input().split())
    if type == 1:
        ans.append(search(ind, x, 1, len_last_layer, 0))
    else:
        update_el(ind, x, 1, len_last_layer, 0)
print(*ans, sep='\n')
