# задания разделяем на четное и нечетное кол-во дней.
# А четные еще разделить на те которые надо сделать в первый день и те
# которые надо во второй день делать (зависит от того сколько простых дней, если с
# первого дня начинать и сколько, если начинать со 2го дня). Так же для каждого задания считаем
# сколько простых дней будет, если идем работаем первым и сколько простых, если вторым. Далее
# надо правильно  отсортировать нечетные. Так чтобы слева у нас были самые выгодные для случая,
# когда в первый день начинаешь, а справа оказались самые выгодные для случая, когда начинаешь
# со второго дня (для этого сортируем по разнице если начинаешь первым минус если начинаешь вторым)
# С четными все просто сначала делаем все выгодные, а невыгодные делаем после смены четности (чтобы они стали выгодными)

n = int(input())
odd = []    # нечет задания 
even_start_first = []   # четные задания
even_start_second = []   # четные задания
for num_task in range(n):
    task = input()
    simple = [0, 0] # кол-во простых дней, если начинаем с первого/второго дня
    for i, s in enumerate(task):
        if s == "S":
            simple[i%2] += 1

    if len(task) % 2 == 0:
        if simple[0] >= simple[1]:
            even_start_first.append(simple)
        else:
            even_start_second.append(simple)
    else:
        odd.append(simple)

odd = sorted(odd, key=lambda x: [x[0]-x[1], (x[0]+x[1])], reverse=True) # сортируем так, что слева оказываются те, что лучше делать когда первым работаешь, а справа наоборот - вторым
second_work = False # False - первым работает, True - вторым работает
ans_simple_days = 0
ans_simple_days += sum(x[second_work] for x in even_start_first)

if odd != []:
    ans_simple_days += odd[0][second_work]
    second_work = True
ans_simple_days += sum(x[second_work] for x in even_start_second)
ind_left, ind_right = 1, len(odd)-1
while ind_left <= ind_right:
    if second_work:
        ans_simple_days += odd[ind_right][second_work]
        ind_right -= 1
    else:
        ans_simple_days += odd[ind_left][second_work]
        ind_left += 1
    second_work = not second_work

print(ans_simple_days)

