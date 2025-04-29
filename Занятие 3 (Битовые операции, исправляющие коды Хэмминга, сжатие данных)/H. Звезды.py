# Используем трехмерное дерево Фенвика (делаем примерно тоже самое, но трижды за log^3(N))
n = int(input())
tree = [[[0]*n for _ in range(n)] for _ in range(n)]

F = lambda i: i & (i+1)
new_ind_update = lambda i: i | (i+1)    # полследний ноль в единицу
while 1:
    request = list(map(int, input().split()))
    if request[0] == 1: # update
        z, y, x, dif = request[1:]
        i = x
        while i < n:
            j = y
            while j < n:
                k = z
                while k < n:
                    tree[i][j][k] += dif
                    k = new_ind_update(k)
                j = new_ind_update(j)
            i = new_ind_update(i)

    elif request[0] == 2: # sum
        def get_sum_cube(z,y,x):
            sum_cube = 0
            i = x
            while i >= 0:
                j = y
                while j >= 0:
                    k = z
                    while k >= 0:
                        sum_cube += tree[i][j][k]
                        k = F(k) - 1
                    j = F(j) - 1
                i = F(i) - 1
            return sum_cube

        # тут из кубика вырезаем все лишнее:
        x1,y1,z1,x2,y2,z2 = request[1:] # x2, y2, z2 по условиям всегда дальше, правее и выше чем x1, y1, z1 (больше или равны)
        sum_x_cube = get_sum_cube(x1-1,y2, z2)  # левей искомого yes
        sum_y_cube = get_sum_cube(x2, y1-1, z2)  # позади искомого yes
        sum_corner_column = get_sum_cube(x1-1, y1-1, z2)    # угловая колонна
        sum_z_cube = get_sum_cube(x2, y2, z1 - 1)  # под искомым кубиком yes
        sum_opposite_corner = get_sum_cube(x1-1, y1-1, z1-1)    # противоположный угол
        sum_down_x = get_sum_cube(x1-1,y2,z1-1)     # ниже левее
        sum_down_y = get_sum_cube(x2, y1-1, z1 - 1) # ниже позади yes

        res_sum = get_sum_cube(x2,y2,z2)    # весь куб с лишними участками
        res_sum -= sum_x_cube   # обрезаем, то что левее
        res_sum -= sum_y_cube           # обрезаем, то что позади
        res_sum += sum_corner_column    # но получится, что колонну мы обрезали дважды, поэтому ее прибавляем
        res_sum -= sum_z_cube           # обрезаем, то что под кубом
        res_sum += sum_down_x           # прибавляем слева снизу (тк вычли дважды: sum_x_cube, sum_z_cube)
        res_sum += sum_down_y           # прибавляем сзади снизу
        res_sum -= sum_opposite_corner  # но противоположный угол прибавили дважды, поэтому его вычитаем
        print(res_sum)

    else:   # == 3 - выход
        break