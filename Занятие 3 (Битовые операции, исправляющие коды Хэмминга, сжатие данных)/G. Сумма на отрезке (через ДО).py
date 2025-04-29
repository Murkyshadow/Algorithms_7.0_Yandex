# 15:31
# решаем через ДО (^_^)

n, q = map(int,input().split())
for i in range(1000000):
    if 2**i >= n:
        break
len_last_layer = 2**i
segment_tree = (len_last_layer-1)*[0] + [0]*n + [0] * (len_last_layer-n)

def get_sum(left, right, now_l, now_r, ind_now): # ищем число >= x, которое не левее данного индекса
    if now_l > right or now_r < left:   # если вне зоны
        return 0
    elif now_l >= left and now_r <= right:    # полностью в хоне поиска
        return segment_tree[ind_now]
    left_child = ind_now*2 + 1
    sum_l = get_sum(left,right,now_l,(now_l+now_r)//2, left_child)   # ищем в левом ребенке
    sum_r = get_sum(left,right,(now_l+now_r)//2+1, now_r, left_child+1)   # ищем в левом ребенке
    return sum_l + sum_r

def update_el(num_new_el, new_el, now_l, now_r, now_ind):   # обновление
    if now_ind >= len(segment_tree) or now_l > num_new_el or now_r < num_new_el:    # вне зоны
        return segment_tree[now_ind]
    if now_l == now_r and now_l == num_new_el:  # нашли элемента
        segment_tree[now_ind] = new_el
        return new_el
    left_child = now_ind*2 + 1
    sum_l = update_el(num_new_el, new_el, now_l, (now_l+now_r)//2, left_child)
    sum_r = update_el(num_new_el, new_el, (now_l + now_r)//2+1, now_r, left_child+1)
    segment_tree[now_ind] = sum_l+sum_r
    return segment_tree[now_ind]

ans = []
for _ in range(q):
    request = input().split()
    if request[0] == 'Q':
        l, r = map(int, request[1:])
        ans.append(get_sum(l,r, 1, len_last_layer, 0))
    else:
        ind, x = map(int, request[1:])
        update_el(ind, x, 1, len_last_layer, 0)
print(*ans, sep='\n')