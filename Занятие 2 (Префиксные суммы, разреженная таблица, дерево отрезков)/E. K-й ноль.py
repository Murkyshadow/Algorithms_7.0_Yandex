# ищем ноль с помощью ДО - в узлах храним кол-во нулей на данном отрезке
n = int(input())
len_nums = 1
while len_nums < n:
    len_nums *= 2

last_layer = list(map(lambda x: int(x) == 0, input().split()))
segment_tree = [None]*(len_nums-1) + last_layer + [0]*(len_nums-n)
for ind in range(len(segment_tree)-len_nums-1, 0-1, -1):
    ind_child_l = ind * 2 + 1
    ind_child_r = ind_child_l + 1
    segment_tree[ind] = segment_tree[ind_child_l]+segment_tree[ind_child_r]

def get_k_zero(end_l, end_r, left_now, right_now, ind_now, k):
    global ans_request
    if ind_now >= len(segment_tree) or left_now > end_r or end_l > right_now or ans_request != -1:    # индекс превышет, нет пересечения или ответ найден
        return 0    
    if left_now == right_now and k == 1 and segment_tree[ind_now] == 1: # нашли наш ноль
        ans_request = ind_now - (len_nums - 1) + 1  # записали в глобальную переменную
        return 1
    if segment_tree[ind_now] < k and end_l <= left_now and end_r >= right_now:   # если в поддереве меньше нулей, чем нужный ноль (k), то возвращаем это кол-во нулей - x и на x нулей ищем меньше
        return segment_tree[ind_now]
    ind_child_left = ind_now * 2 + 1
    # считаем сколько нулей мы прошли
    count_zero = get_k_zero(end_l, end_r, left_now, (right_now+left_now)//2, ind_child_left, k)  # если в левом ребенке не было нашего нуля, то записываем сколько там было нулей (на искомом участке)
    # и теперь в правом ребенке мы ищем не k-ый ноль, а k-x ноль (тк x нулей было в левом)
    count_zero += get_k_zero(end_l, end_r, (right_now + left_now) // 2 + 1, right_now, ind_child_left+1, k-count_zero)
    return count_zero

def update_segment_tree(num_el, new_el, now_l, now_r, now_ind): # обновление очень похоже на прошлую задачу
    if now_ind >= len(segment_tree):
        return 0
    if now_l > num_el or now_r < num_el: # не пересекает
        return segment_tree[now_ind]
    elif num_el == now_l and num_el == now_r:   # наш элемент
        segment_tree[now_ind] = (new_el == 0)
        return (new_el == 0)
    ind_child_l = now_ind*2 + 1
    res_left = update_segment_tree(num_el, new_el, now_l, (now_r + now_l) // 2, ind_child_l)
    res_right = update_segment_tree(num_el, new_el, (now_r + now_l) // 2 + 1, now_r, ind_child_l + 1)
    segment_tree[now_ind] = res_right + res_left
    return segment_tree[now_ind]

ans = []

for _ in range(int(input())):   # обрабатываем запросы
    ans_request = -1
    query = input().split()     # request
    if query[0] == 's':
        left_segment, right_segment, k = map(int, query[1:])
        get_k_zero(left_segment, right_segment, 1, len_nums, 0, k)
        ans.append(ans_request)
    else:
        update_segment_tree(int(query[1]), int(query[2]), 1, len_nums, 0)
        last_layer[int(query[1])-1] = (int(query[2]) == 0)

print(*ans)
