# решается так же как прошлые 2 задачи
# единственное в задаче указано, что мы удаляем ребра
# но так же написано, что в конце не останется ребер
# так почему бы нам просто не пойти с конца запрос и тогда получится,
# что вместо удаления мы будем наоборот соединять --> задача сведена к прошлым 2м

n, m, k = map(int, input().split())
sets = [set([i]) for i in range(n)]  # храним связанные вершины в одном множестве
num_set_vertex = list(range(n))    # для каждой вершины храним в каком множестве она находится (изначально у каждоой вершины свое множество), используем этот массив для ответа на ask
edges = [input() for _ in range(m)] # не пригодиться
requests = [input() for _ in range(k)]  # запросы
ans = []
for _ in range(k):
    type, vertex_1, vertex_2 = requests.pop().split()   # обрабатываем запросы с конца
    vertex_1, vertex_2 = int(vertex_1) - 1, int(vertex_2) - 1
    if type == 'cut':   # если идем с конца, то выполняем обратное действие - соединяем 2 ребра
        if num_set_vertex[vertex_1] != num_set_vertex[vertex_2]:   # объединяем только если вершины находятся в разных множествах
            if len(sets[num_set_vertex[vertex_1]]) > len(sets[num_set_vertex[vertex_2]]):    # объединяем множества связанных вершин (при этом меньшее множество кладем в большее)
                ind_set_for_del = num_set_vertex[vertex_2]  # из меньшего удаляем
                ind_set_for_add = num_set_vertex[vertex_1]  # в большее добавляем
            else:
                ind_set_for_del = num_set_vertex[vertex_1]
                ind_set_for_add = num_set_vertex[vertex_2]
            while len(sets[ind_set_for_del]) > 0:   # объединяем множества (из меньшего переносим эл. в большее)
                del_el = sets[ind_set_for_del].pop()
                sets[ind_set_for_add].add(del_el)
                num_set_vertex[del_el] = ind_set_for_add
            sets[ind_set_for_del] = None    # удаляем пустое множество, чтобы выйграть по памяти (если использовать списки - они занимают меньше места (праоверено✔))
    else:   # ask
        ans.append('YES' if num_set_vertex[vertex_1] == num_set_vertex[vertex_2] else 'NO') # записываем ответ

print(*ans[::-1], sep='\n')