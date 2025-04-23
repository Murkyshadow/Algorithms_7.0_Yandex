# опять используем ДО
# Храним в каждом изле три числа: максимум нулей на отрезке, кол-во нулей подряд начиная слева (префикс), кол-во нулей начиная справа (суфикс)
n = int(input())
len_last_layer = 1
while len_last_layer < n:
    len_last_layer *= 2

len_now_layer = len_last_layer // 2
count_layers = 1
rating = [[0,0,0] for _  in range(len_last_layer-1)] + list(map(lambda x: [1,1,1] if x=='0' else [0,0,0], input().split())) + [[0,0,0] for _ in range(len_last_layer-n)]    # segment_tree: [[max, pref, suf], [],...]
end_layer = len_last_layer-2 - len_now_layer
for i in range(len_last_layer-2, 0-1, -1):
    if end_layer == i:  # подсчитываем уровень, чтобы определить длину текущего отрезка
        count_layers += 1
        len_now_layer //= 2
        end_layer -= len_now_layer
    left_child = i*2 + 1
    # новый максимум равен либо правому максимум, либо левосу или сумме левого суффикса и правого префекса
    rating[i][0] = max([rating[left_child][0], rating[left_child+1][0], rating[left_child][2]+rating[left_child+1][1]])
    diapazone_child = 2 ** (count_layers-1) # длина текущего отрезка
    # новый префекс равен либо префексу левого, либо если левый полностью состоял из нулей (кол-во нулей = длине), то длине левого + префекса правого
    rating[i][1] = rating[left_child][1] if diapazone_child != rating[left_child][0] else rating[left_child][0] + rating[left_child+1][1]
    # новый суффикс равен либо суффиксу правого, либо если правый полностью состоял из нулей, то сумме длины правого + суфикса левого
    rating[i][2] = rating[left_child+1][2] if diapazone_child != rating[left_child+1][0] else rating[left_child+1][0] + rating[left_child][2]

def get_max_sequence(search_l, search_r, now_l, now_r, now_ind):
    if search_l > now_r or now_l > search_r:
        return -1, 0
    if search_l <= now_l and search_r >= now_r: # полностью
        return rating[now_ind], (now_r-now_l)+1
    left_child = now_ind*2 + 1
    left_return, len_left = get_max_sequence(search_l,search_r,now_l,(now_r+now_l)//2,left_child)
    right_return, len_right = get_max_sequence(search_l,search_r,(now_r+now_l)//2 + 1, now_r, left_child+1)

    best_max_sequence = [0,0,0] # [max, pref, suf]
    res_len = len_left + len_right
    # пересчитываем длину так же как при составлении дерева
    if left_return != -1 and right_return != -1:    # если ретюрн из ненужного, который учитывать не надо
        best_max_sequence[0] = max([left_return[0], right_return[0], left_return[2]+right_return[1]])    # max
        best_max_sequence[1] = left_return[1] if len_left != left_return[0] else left_return[0] + right_return[1]    # pref
        best_max_sequence[2] = right_return[2] if len_right != right_return[0] else right_return[0] + left_return[2]    # suf
    elif left_return == -1 and right_return != -1:  # если левый участок не входил в искомую зону, то учитываем только правый
        best_max_sequence = right_return
        res_len = len_left
    else:   # если правый участок не входил в искомую зону, то учитываем только левый
        best_max_sequence = left_return
        res_len = len_right

    return best_max_sequence, res_len

def update_rating(search_num_el, new_el, now_left, now_right, now_ind):
    if search_num_el > now_right or search_num_el < now_left:
        return rating[now_ind]
    if now_left == now_right and now_left == search_num_el:
        rating[now_ind] = [int(new_el==0)]*3
        return rating[now_ind]

    left_child = now_ind * 2 + 1
    left_return = update_rating(search_num_el, new_el, now_left, (now_right + now_left) // 2, left_child)
    right_return = update_rating(search_num_el, new_el, (now_right + now_left) // 2 + 1, now_right, left_child + 1)
    best_max_sequence = [0, 0, 0]  # [max, pref, suf]
    diapazone_child = ((now_right - now_left) + 1) // 2
    best_max_sequence[0] = max([left_return[0], right_return[0], left_return[2] + right_return[1]])  # max
    best_max_sequence[1] = left_return[1] if diapazone_child != left_return[0] else left_return[0] + right_return[1]  # pref
    best_max_sequence[2] = right_return[2] if diapazone_child != right_return[0] else right_return[0] + left_return[2]  # suf
    rating[now_ind] = best_max_sequence
    return rating[now_ind]

ans = []
for _ in range(int(input())):
    request = input().split()
    if request[0] == 'QUERY':
        l, r = map(int, request[1:])
        ans.append(get_max_sequence(l, r, 1, len_last_layer, 0)[0])
    else:
        ind, x = map(int, request[1:])
        update_rating(ind, x, 1, len_last_layer, 0)

print(*[int(x[0]) for x in ans], sep='\n')
