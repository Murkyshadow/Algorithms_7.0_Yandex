# просто начитаем все комбинации чисел и сравним их
num = int(input())
num_in_binary = str(bin(num)[2:])

all_two_in_degree = [1]
now_two_in_degree = 1
while now_two_in_degree < num:  # насчитаем все степени двойки заранее, чтобы сэконоить немного во времени (хотя и без этого зайдет)
    now_two_in_degree *= 2
    all_two_in_degree.append(now_two_in_degree)

ans = 0
for st_ind in range(-len(num_in_binary), 0):
    num_digit = len(num_in_binary)-1   # номер разряда
    now_num = 0
    for now_digit in range(st_ind, len(num_in_binary)+st_ind):  # тут используем отрицательные индексы, чтобы удобно проходить по числу
        if num_in_binary[now_digit] == '1':
            now_num += all_two_in_degree[num_digit]
        num_digit -= 1
    ans = max([ans, now_num])

print(ans)