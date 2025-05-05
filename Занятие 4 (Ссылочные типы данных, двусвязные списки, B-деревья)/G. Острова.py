# аналогично прошлому решению
# точно так же как и в прошлой задаче идем по парам (острова, которые соединяет каждая дорога) и объединяем множество
# островов (если они находятся в разных множествах) до тех пор пока у нас не получится одно множество (ну, еще кол-во дорог считаем)
n, m = map(int, input().split())
sets = [set([i]) for i in range(n)]  # храним связанные острова в одном множестве
num_set_island = list(range(n))    # для каждого острова храним в каком множестве он находится (изначально у каждого острова свое множество)
count_sets = n  # кол-во не пустых последовательностей (множеств)
for num_bridge in range(1,m+1):
    first_island, second_island = map(lambda x: int(x)-1, input().split())
    if num_set_island[first_island] != num_set_island[second_island]:   # объединяем только если острова находятся в разных множествах
        if len(sets[num_set_island[first_island]]) > len(sets[num_set_island[second_island]]):    # объединяем множества островов (при этом меньшее множество кладем в большее)
            ind_set_for_del = num_set_island[second_island]   # из меньшего удаляем
            ind_set_for_add = num_set_island[first_island]    # в большее добавляем
        else:
            ind_set_for_del = num_set_island[first_island]
            ind_set_for_add = num_set_island[second_island]
        while len(sets[ind_set_for_del]) > 0:   # объединяем множества (из меньшего переносим эл в большее)
            del_el = sets[ind_set_for_del].pop()
            sets[ind_set_for_add].add(del_el)
            num_set_island[del_el] = ind_set_for_add
        sets[ind_set_for_del] = None    # удаляем пустое множество, чтобы выйграть по памяти (а если еще использовать списки - они занимают меньше места (праоверено✔))
        count_sets -= 1
        if count_sets == 1:
            print(num_bridge)
            break

