# для данной задачи дерево отрезков не пойдойдет, так как дерево отвечает на запрос за О(log(N))
# а учитывая, что у нас K запросов получаем О(K*log(N)), поэтому через дерево может не зайти (хотя не пробовал)
# поэтому использовал рязреженную таблицу
n = int(input())
nums = [[]]
nums[0] = list(map(lambda x: [int(x[1]), x[0]], enumerate(input().split(), 1))) # в таблице храним максимум и его индекс
step = 1
y = 1
while step < len(nums[y-1]):
    nums.append([])
    for i in range(len(nums[y-1])-step):    # заполняем строки таблицы
        nums[-1].append(max([nums[y-1][i], nums[y-1][i+step]])) # выбираем максимум на отрезке
    step *= 2
    y += 1

step_for_num = {}
step = 0
num_step = 1
for num in range(1,n+1):
    if num >= num_step:
        step += 1
        num_step *= 2
    step_for_num[num] = step-1

for _ in range(int(input())):
    l, r = map(int,input().split())
    print(max([nums[step_for_num[r-l+1]][l-1], nums[step_for_num[r-l+1]][r-2**step_for_num[r-l+1]]])[1])    # отвечаем на запрос за O(1)
