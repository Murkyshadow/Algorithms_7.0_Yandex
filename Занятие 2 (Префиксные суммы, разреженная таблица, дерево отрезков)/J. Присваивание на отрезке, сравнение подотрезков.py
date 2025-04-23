# ДО, храним в узлах хеш текущего отрезка, ВСЕ подсчеты по модулю
# чуть более простой вариант решения был показан в разборе лекции
def start(n, nums, x=13):
    len_last_layer = 1
    while len_last_layer < n:
        len_last_layer *= 2

    hashs = []
    x_in_degree = [x**0]*(n+1)
    pref_sum_x_in_degree = [0]
    for degree, num in enumerate(nums, 1):
        x_in_degree[degree] = (x_in_degree[degree-1] * x) % p
        pref_sum_x_in_degree.append((pref_sum_x_in_degree[-1]+x_in_degree[degree]) % p)   # без нулевой степени
        hashs.append((num*x_in_degree[degree])%p)   # считаем хэш - a[i] * x**i по модулю

    segment_tree = [None] * (len_last_layer-1) + hashs + [0] * (len_last_layer-n)   # в узлах храним хэши чисел и считаем их суммы
    for ind in range(len_last_layer-2, 0-1, -1):
        left_child = ind*2 + 1
        segment_tree[ind] = (segment_tree[left_child] + segment_tree[left_child+1]) % p   # сумма левого и правого
    return segment_tree, pref_sum_x_in_degree, x_in_degree, len_last_layer

def get_hash_segment(left, right, now_left, now_right, now_ind, new_num):
    if new_num != None:
        sum_x_in_degree = (pref_sum_x_in_degree[now_right] - pref_sum_x_in_degree[now_left-1]) % p  # ну, тут если первое меньше второго, то все может пойти через жопу, но надеюсь такого не будет
        segment_tree[now_ind] = (new_num * sum_x_in_degree) % p  # ищем новый хэш
        promises_child[now_ind] = new_num   # и обещаем детям присвоить новый хэш

    if left > now_right or right < now_left:    # не пересекает
        return 0
    if left <= now_left and right >= now_right:
        return segment_tree[now_ind]

    left_child = now_ind * 2 + 1
    return_left = get_hash_segment(left,right,now_left,(now_left+now_right)//2, left_child, promises_child[now_ind])
    return_right = get_hash_segment(left, right, (now_left + now_right) // 2 + 1, now_right, left_child+1, promises_child[now_ind])
    promises_child[now_ind] = None  # обещание передали левому и правому --> обещание выполнено
    return (return_left + return_right) % p

def update_segment(new_el,left,right,now_left,now_right,ind, promise=None):
    if promise != None:
        promises_child[ind] = promise
        sum_x_in_degree = (pref_sum_x_in_degree[now_right] - pref_sum_x_in_degree[now_left - 1]) % p  # ну, тут если первое меньше второго, то все может пойти через жопу, но надеюсь такого не будет
        segment_tree[ind] = (promise * sum_x_in_degree) % p  # ищем новый хэш
    if left > now_right or right < now_left:    # вне зоны
        return segment_tree[ind]

    if left <= now_left and right >= now_right: # полностью накрыло
        promises_child[ind] = new_el
        sum_x_in_degree = (pref_sum_x_in_degree[now_right] - pref_sum_x_in_degree[now_left - 1]) % p  # ну, тут если первое меньше второго, то все может пойти через жопу, но надеюсь такого не будет
        segment_tree[ind] = (new_el * sum_x_in_degree) % p  # ищем новый хэш
        return segment_tree[ind]

    left_child = ind*2 + 1
    return_l = update_segment(new_el, left, right, now_left, (now_left+now_right)//2,left_child, promises_child[ind])
    return_r = update_segment(new_el, left, right, (now_left+now_right)//2 + 1, now_right, left_child+1, promises_child[ind])
    promises_child[ind] = None
    segment_tree[ind] = (return_r+return_l)%p
    return segment_tree[ind]

p = 10**9 + 7
n = int(input())
nums = list(map(int, input().split()))
q = int(input())

segment_tree, pref_sum_x_in_degree, x_in_degree, len_last_layer = list(start(n, nums, 13))
promises_child = [None]*len(segment_tree)    # обещания детям, изначально все выполнены

ans = ''
for i in range(q):
    t, l, r, k = map(int, input().split())
    if t == 1:  # сравнение
        l, r = min([l, r]), max([l, r]) # l не обязательно меньше r по условию
        hash_first_seg = (get_hash_segment(l, l+k-1, 1, len_last_layer, 0, None) * x_in_degree[r-l]) % p
        hash_second_seg = get_hash_segment(r, r+k-1, 1, len_last_layer, 0, None)
        if hash_first_seg == hash_second_seg:
            ans_1 = '+'
        else:
            ans_1 = '-'
        ans += ans_1
    else:   # t=0 переприсвоение чисел
        update_segment(k, l, r, 1, len_last_layer, 0)

print(ans,end='')
