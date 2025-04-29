# есть несколько способов решения данной задачи, но у меня был следующий:
# насчитываем кол-во единиц и ноликов для каждого числа, дальше идем по столбикам (выбираем единицу или нолик
# для 1го рязряда каждого числа, потом для 2го разряда каждого числа и тд), но встает вопрос, как выбрать
# но без разницы что мы выбираем, лишь важно чтобы в самом последне (нижнем) числе можно выбрать ноль или один
# Но что делать если в последнем числе остались только нолики или только единицы?
# Мы просто идем снизу вверх применяем XOR с каждым число, где нет выбора
# (самое последнее (первое с конца) число xor на 0 тк мы к нулю стремимся) и идём
# до тех пор пока не встретим число с развилкой
# Потом идём сверху выбирая в целом любые числа (но если есть выбор, то выбирать лучше тех что больше) и
# идём до последнего числа с развилкой и выбираем то число (0 или 1), которое получилось в результате xor снизу

n = int(input())
nums = list(map(int,input().split()))

max_num = max(nums)
max_num_digit = 1
all_two_in_degree = [1,2]
while all_two_in_degree[-1] <= max_num:
    all_two_in_degree.append(all_two_in_degree[-1] * 2)
    max_num_digit += 1  # кол-во разрядов

def get_one(num, max_num_digit=max_num_digit):  # получаем кол-во единиц и нулей в числе
    two_in_degree = 1
    while two_in_degree <= num:
        two_in_degree *= 2
    two_in_degree //= 2
    count_one = 0
    while num > 0:
        if two_in_degree <= num:
            num -= two_in_degree
            count_one += 1
        two_in_degree //= 2
    return [max_num_digit-count_one,count_one]

count_zero_one = list(map(get_one, nums))   # кол-во единиц и ноликов в каждом числе
ans = [0]*n    # ответ
for num_digit in range(max_num_digit):  # номер разряда
    ind_last_num = n    # последнее с конца число, у которого нет развилки (нет единиц или нет ноликов)
    need_get_on_last_num = 0
    for i in range(n-1, 1-1, -1):   # ищем первую развилку (где есть ноль и единица), не доходя до нуля (первого числа)
        if count_zero_one[i][1] == 0:   # если нет единиц, то будем использовать ноль и должны получить ответ ^=0
            need_get_on_last_num ^= 0
            count_zero_one[i][0] -= 1
        elif count_zero_one[i][0] == 0:   # если нет нулей, то будем использовать единцу и ответ ^=1
            need_get_on_last_num ^= 1
            count_zero_one[i][1] -= 1
            ans[i] += all_two_in_degree[num_digit]
        else:
            break
        ind_last_num = i    # если не брейк, то новый индекс

    now_digit = 0   # начальное берем за ноль тк разряд первого числа не должен изменится 0^1=1  0^0=0
    for i in range(ind_last_num):
        if ind_last_num-1 == i: # последний слой, на котором есть развилка (и нолик и единица)
            if need_get_on_last_num == 0:   # нужно получить ноль
                if now_digit == 1 and count_zero_one[i][1] != 0:  # если нужен ноль, а сейчас единица, то на что нужно заXORить, чтобы получить ноль?  1^? = 0  ?=1
                    ans[i] += all_two_in_degree[num_digit]
                    count_zero_one[i][1] -= 1
                elif now_digit == 0 and count_zero_one[i][0] != 0:  # 1^?=0 ?=0 используем 0
                    count_zero_one[i][0] -= 1
                else:
                    ans = 'impossible'
                    break
            else:   # нужно получить один
                if now_digit == 1 and count_zero_one[i][0] != 0:  # если нужна единиц, а сейчас единица, то на что нужно заXORить, чтобы получить единицу?  1^? = 1  ?=0
                    count_zero_one[i][0] -= 1
                elif now_digit == 0 and count_zero_one[i][1] != 0:  # 0^? = 1  ?=0 используем 1
                    ans[i] += all_two_in_degree[num_digit]
                    count_zero_one[i][1] -= 1
                else:
                    ans = 'impossible'
                    break
        else:   # выбираем тех кого больше
            if count_zero_one[i][1] > count_zero_one[i][0]:  # если единиц больше нулей, то берем единицы (чтобы не сложилась такая ситуация в конце, что остались только нолики или только единицы)
                count_zero_one[i][1] -= 1
                ans[i] += all_two_in_degree[num_digit]
                now_digit ^= 1
            else:  # иначе нолик
                count_zero_one[i][0] -= 1
                now_digit ^= 0

    if ans == 'impossible':
        print(ans)
        break

if ans != 'impossible':
    print(*ans)