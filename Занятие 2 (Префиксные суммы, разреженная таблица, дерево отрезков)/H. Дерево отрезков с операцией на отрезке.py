# опять ДО только теперь изменяем сразу отрезок
n = int(input())
len_last_layer = 1
while len_last_layer < n:
    len_last_layer *= 2

segment_tree = [None] * (len_last_layer-1) + list(map(int, input().split())) + [-1] * (len_last_layer-n)
for i in range(len_last_layer-2, 0-1, -1):
    left_child = i*2 + 1
    segment_tree[i] = max([segment_tree[left_child], segment_tree[left_child+1]])

def get_num(num_el, now_left, now_right, ind, add):
    segment_tree[ind] += add    # выполняем обещание
    promises_childs[ind] += add # и обещаем детям
    if num_el < now_left or num_el > now_right:
        return
    if now_left == now_right and num_el == now_right:   # нашли искомый элемент и записали его
        global search_num
        search_num = segment_tree[ind]
        return

    left_child = ind*2 + 1
    get_num(num_el, now_left, (now_left+now_right)//2, left_child, promises_childs[ind])
    get_num(num_el, (now_left+now_right)//2 + 1, now_right, left_child+1, promises_childs[ind])
    promises_childs[ind] = 0
    return

def upadte_segment(add_num, up_left, up_right, now_left, now_right, ind):
    if up_left > now_right or up_right < now_left:
        return segment_tree[ind]
    # если искомый отрезок полностью покрывает текущий, то обнавляем значение на текущем отрезке и обещаем обновить детей (потом)
    elif now_left >= up_left and now_right <= up_right:
        promises_childs[ind] += add_num
        segment_tree[ind] += add_num
        return segment_tree[ind]

    left_child = ind*2 + 1
    l_return = upadte_segment(add_num, up_left, up_right, now_left, (now_left+now_right)//2, left_child)
    r_return = upadte_segment(add_num, up_left, up_right, (now_left+now_right)//2 + 1, now_right, left_child+1)
    segment_tree[ind] = max([l_return, r_return])
    return segment_tree[ind]

search_num = -1
promises_childs = [0]*len(segment_tree)    # храним обещание для каждого элемента (обещеание предназначено для детей этого элемента)
ans = []
for _ in range(int(input())):
    request = input().split()
    if request[0] == 'g':
        num_el = int(request[1])
        get_num(num_el, 1, len_last_layer, 0, 0)
        ans.append(search_num)
    else:
        l,r,add_num = map(int, request[1:])
        upadte_segment(add_num, l,r, 1,len_last_layer,0)
print(*ans, sep='\n')
