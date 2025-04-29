# сдавать только на python (pypy не прошел)
# Построим три проекции расстановки ладей на грани куба. Тогда, фиксированная клетка (x,y,z) бьется хотя бы одной ладьей, если какая-то из ладей бьет хотя бы одну из клеток
# (x,y), (y,z), (x,z) на соответствующих проекциях (в yz yx zx храним какие столбики бьют ладьи)
# Таким образом, проверку одной клетки можно организовать за O(1). Проходимся по всем клеткам за N^3 и проверяем бьется ли каждая из клеток хоть одним столбиком
# Но такое решение работает за время N^3 и при заданных ограничениях на N не проходит по времени.
# Чтобы оптимизировать решение, можно использовать битовые операции,
# тогда за одну операцию мы проверим сразу несколько клеток


n, k = map(int, input().split())
all_two_in_degree = [1]
now_two_in_deree = 1
degree = 1
while degree <= n:
    now_two_in_deree *= 2
    all_two_in_degree.append(now_two_in_deree)
    degree += 1

yz = [0]*n  # y - номер в массиве, z - номер разряда
yx = [0]*n  # y - номер в массиве, x - номер разряда
zx = [0]*n  # z - номер в массиве, x - номер разряда
for i in range(k):
    x,y,z = map(int, input().split())
    yz[y-1] |= all_two_in_degree[z-1]
    yx[y-1] |= all_two_in_degree[x-1]
    zx[z-1] |= all_two_in_degree[x-1]

ans = 'YES'
for y in range(n):
    for z in range(n):
        if (yz[y] & all_two_in_degree[z]) == 0:
            two_projection = yx[y] | zx[z]
            if (two_projection) != all_two_in_degree[n]-1:
                ans = 'NO'
                bin_num_s = bin(two_projection)[:1:-1] # обрезаем 2 лишних символа "0b" и разворачиваем разряды, чтобы нумеровались слева напрво
                x_first_zero = (bin_num_s + ((n-len(bin_num_s))*'0')).find('0') + 1   # добавляем недостоющие нули и прибавляем 1 тк нумерация с одного
                print(ans)
                print(x_first_zero, y+1, z+1)
                break
    if ans == 'NO':
        break

if ans != 'NO':
    print(ans)