# 2ое решение через ДФ
# если сравнивать с ДО, то работает быстрей, да и пишется легче

n, q = map(int,input().split())
nums = [0] * n
tree = [0] * n   # ДФ

def get_sum_on_pref(ind):
    sum = 0
    while ind >= 0:
        sum += tree[ind]
        ind = F(ind) - 1
    return sum

F = lambda i:  i & (i+1)    # убирает единицы с конца (для суммы)
for i in range(q):
    request = input().split()
    if request[0] == 'A':   # = new_num
        now_ind, new_num = map(int,request[1:])
        now_ind -= 1    # нумерация с нуля
        dif = new_num - nums[now_ind]   # разница сежду прошлым и текущим
        nums[now_ind] += dif    # так же обновляем исходный массив, чтобы потом находить разницу чисел
        while now_ind < len(tree):
            tree[now_ind] += dif
            now_ind = now_ind | (now_ind+1) # последний поль заменяем на единицу и этот элемент будет включать эл который надо было заменить
    else: # sum
        l, r = map(int,request[1:])
        print(get_sum_on_pref(r-1) - get_sum_on_pref(l-2))
