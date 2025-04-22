# Для решение данной задачи я реализовал дерево отрезков с возможностью
# получения кол-ва максимумов на отрезке
import math

n = int(input())
len_nums = 1
while len_nums < n:
    len_nums *= 2
# создаем дерево отрезков, в узлах храними 2 числа [максимум, кол-во максимумов], на последнем слое дерева для каждого числа всего один максимум - он сам
nums = [None]*(len_nums-1) + list(map(lambda x: [int(x), 1], input().split())) + [[-math.inf,-math.inf]]*(len_nums-n)   # элементы для первых слоев + данные элементы + недостающие элементы последнего слоя (len_last_layer = 2**p)
for ind in range(len(nums)-len_nums-1, 0-1, -1):    # для каждого элемента ищем максимальный элемент и его кол-во через его детей
    ind_child_l = ind * 2 + 1
    ind_child_r = ind_child_l + 1
    count_max = 0
    count_max = max([nums[ind_child_l],nums[ind_child_r]])[1]   # берем наибольший максиму ребенка и его кол-во на отрезке
    if nums[ind_child_l][0] == nums[ind_child_r][0]:   # если максимумы равны, то кол-во максимумов - это сумма детей
        count_max = nums[ind_child_l][1] + nums[ind_child_r][1]
    nums[ind] = [max(nums[ind_child_l][0], nums[ind_child_r][0]), count_max]

# получение кол-ва максимумов через рекурсию, по факту углубляемся в дерево до тех пор пока искомый отрезок не будет полностью покрывать или не покрывать искомый
def get_max(l, r, now_ind, left_section, right_section):
    if now_ind > len(nums)-1 or r < left_section or right_section < l:   # то, что ищем не пересекается с текущим отрезком
        return [-math.inf, -math.inf]   # возвращаем нейтральный элемент
    elif l <= left_section and r >= right_section:  # текущий отрезок полностью входит в искомый
        return nums[now_ind]    # возвращаем текущий элемент
    # если текущий отрезок не целиком входит в искомый, то обращаемся к детям
    ind_child_l = now_ind * 2 + 1
    max_l = get_max(l, r, ind_child_l, left_section, (left_section+right_section)//2)
    max_r = get_max(l, r, ind_child_l+1, (left_section+right_section)//2+1, right_section)
    if max_r[0] == max_l[0]:    # если у детей максимумы совпадают, то возвращаем сумму их количеств максимумов
        return [max_l[0], max_r[1] + max_l[1]]
    return max([max_r, max_l])

for _ in range(int(input())):   # обрабатываем запросы
    left_ind, right_ind = map(int,input().split())
    print(*get_max(left_ind-1, right_ind-1, 0, 0, len_nums-1))  # ищем кол-во максимумов на заданном отрезке
