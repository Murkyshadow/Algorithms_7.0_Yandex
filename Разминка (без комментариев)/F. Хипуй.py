def Insert(num):
    heap.append(num)
    now_ind = len(heap)-1
    while now_ind != 0 and heap[(now_ind-1) // 2] < num:
        heap[(now_ind - 1) // 2], heap[now_ind] = heap[now_ind], heap[(now_ind-1) // 2]
        now_ind = (now_ind-1) // 2

def Extract():
    del_num = heap[0]
    heap[0] = heap[-1]
    now_ind = 0
    while len(heap) > now_ind*2 + 2:
        ind_max_num = now_ind * 2 + 1
        if heap[now_ind*2 + 1] < heap[now_ind*2 + 2]:
            ind_max_num = now_ind*2 + 2
        if heap[now_ind] < heap[ind_max_num]:
            heap[now_ind], heap[ind_max_num] = heap[ind_max_num], heap[now_ind]
            now_ind = ind_max_num
        else:
            break
    heap.pop()
    return del_num

heap = []
n = int(input())
for _ in range(n):
    command = list(map(int, input().split()))
    if command[0] == 1:
        print(Extract())
    else:
        Insert(command[1])