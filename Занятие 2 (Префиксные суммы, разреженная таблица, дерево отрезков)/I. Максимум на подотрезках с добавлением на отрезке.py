# опять ДО и единственное отличие от прошлой задачи - увеличиваем элементы
n = int(input())
len_last_layer = 1
while len_last_layer < n:
    len_last_layer *= 2

nums = list(map(int, input().split()))
segment_tree = [None] * (len_last_layer-1) + nums + [-1] * (len_last_layer-n)
for i in range(len_last_layer-2, 0-1, -1):
    left_child = i*2 + 1
    segment_tree[i] = max([segment_tree[left_child], segment_tree[left_child+1]])

def get_num(left, right, now_left, now_right, ind, add):
    segment_tree[ind] += add    # выполняем обещание
    promises_childs[ind] += add # и обещаем детям
    if right < now_left or left > now_right:
        return 0
    if right >= now_right and left <= now_left:
        return segment_tree[ind]

    left_child = ind*2 + 1
    left_return = get_num(left, right, now_left, (now_left+now_right)//2, left_child, promises_childs[ind])
    right_return = get_num(left, right, (now_left+now_right)//2 + 1, now_right, left_child+1, promises_childs[ind])
    promises_childs[ind] = 0
    return max([left_return,right_return])

def update_segment(add_num, up_left, up_right, now_left, now_right, ind):
    # при обновлении обещания могут накапливаться, поэтому прибавляем обещания и если встречаем на пути обещание, то выполняем его
    if up_left > now_right or up_right < now_left:
        promises_childs[ind] += promises_childs[(ind-1)//2]
        segment_tree[ind] += promises_childs[(ind-1)//2]
        return segment_tree[ind]
    elif now_left >= up_left and now_right <= up_right:
        promises_childs[ind] += add_num + promises_childs[(ind-1)//2]
        segment_tree[ind] += add_num + promises_childs[(ind-1)//2]
        return segment_tree[ind]

    left_child = ind*2 + 1
    promises_childs[ind] += promises_childs[(ind-1)//2] # добавляем обещание предка
    l_return = update_segment(add_num, up_left, up_right, now_left, (now_left+now_right)//2, left_child)
    r_return = update_segment(add_num, up_left, up_right, (now_left+now_right)//2 + 1, now_right, left_child+1)
    promises_childs[ind] = 0
    segment_tree[ind] = max([l_return, r_return])
    return segment_tree[ind]

promises_childs = [0]*len(segment_tree)
ans = []
for i in range(int(input())):
    request = input().split()
    if request[0] == 'm':
        l, r  = map(int, request[1:])
        ans.append(get_num(l,r, 1, len_last_layer, 0, 0))
    else:
        l,r,add_num = map(int, request[1:])
        update_segment(add_num, l,r, 1,len_last_layer,0)
print(*ans)
