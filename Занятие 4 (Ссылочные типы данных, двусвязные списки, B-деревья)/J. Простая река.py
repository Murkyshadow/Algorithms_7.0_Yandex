# нам нужна структура, в которую можно быстро вставлять элмент (при разделении фирмы)
# и быстро удалять элемент (при банкротстве фирмы)
# так же нам нужно было бы быстро обращаться к элементу, если бы не жирное условие (см. условия задачи)
# соласно которому следующее событие происходит в фирме не подалеку (не дальше 10ой)
# и зная это, нам нужно просто сохранить ссылку на последнюю фирму (с которой произошло событие)
# и от него мы сможем быстро добраться до след. фирмы (с которым произойдет событие)
# с этой задачей отлично справиться двусвязный список

class Doubly_list():
    def __init__(self, length, left, right):
        self.length = length
        self.left_firm = left
        self.right_firm = right

n, p = map(int, input().split())
lenghts_firms = list(map(lambda l: Doubly_list(int(l), None, None), input().split()))
now_firm = lenghts_firms[0]
now_firm.right_firm = lenghts_firms[1]
for i, l in enumerate(lenghts_firms[1:-1], 1):
    lenghts_firms[i].left_firm = lenghts_firms[i-1]
    lenghts_firms[i].right_firm = lenghts_firms[i+1]
lenghts_firms[-1].left_firm = lenghts_firms[-2]
now_tax = sum([l.length**2 for l in lenghts_firms]) # сумма квадратов длин отрезков реки предприятий
del lenghts_firms
print(now_tax)
now_num_firm = 1    # текущий номер предприятия
for _ in range(int(input())):
    type, need_num_firm = map(int, input().split())
    while need_num_firm != now_num_firm:    # находим нужное предприятие
        now_firm = now_firm.right_firm if now_num_firm < need_num_firm else now_firm.left_firm
        now_num_firm += 1 if now_num_firm < need_num_firm else -1
    left_firm = now_firm.left_firm
    right_firm = now_firm.right_firm
    len_left_part = now_firm.length // 2  # делим отрезок реки на 2
    len_right_part = now_firm.length // 2 + (now_firm.length % 2)  # если длина нечетная, то прибавляем единицу тому что провее (дальше от истока)
    now_tax -= now_firm.length ** 2  # вычитаем налог обанкротившегося/разделившегося
    if type == 1: # обанкротилось
        if left_firm == None:  # первое предприятие обанкротилось
            now_tax -= right_firm.length**2 # вычитаем налог правого
            now_tax += (right_firm.length + now_firm.length) ** 2 # прибавляем новый налог правого
            right_firm.length += now_firm.length  # правому достается вся длина
            right_firm.left_firm = left_firm    # = None
            now_firm = right_firm   # правое стало первым (номер предприятия не поменялся)
        elif right_firm == None:   # последнее предприятие обанкротилось
            now_tax -= left_firm.length ** 2    # вычитаем налог левого
            now_tax += (left_firm.length + now_firm.length) ** 2  # прибавляем новый налог левого
            left_firm.length += now_firm.length  # левому достается вся длина
            left_firm.right_firm = right_firm   # = None
            now_firm = left_firm
            now_num_firm -= 1   # текущий номер предприятия стал на 1 меньше
        else:
            now_tax -= right_firm.length ** 2  # вычитаем налог правого
            now_tax -= left_firm.length ** 2    # вычитаем налог левого
            now_tax += (right_firm.length + len_right_part) ** 2  # прибавляем новый налог правого
            now_tax += (left_firm.length + len_left_part) ** 2  # прибавляем новый налог левого
            right_firm.length += len_right_part  # правому достается правая половина обанкротившегося (возможно на 1 больше)
            left_firm.length += len_left_part # левому достается левая половина обанкротившегося

            right_firm.left_firm = left_firm    # новые указатели
            left_firm.right_firm = right_firm
            now_firm = left_firm
            now_num_firm -= 1
    else:   # разделилось
        now_tax += len_left_part**2 + len_right_part**2 # прибавляем налог новых предприятий
        new_left_firm = Doubly_list(len_left_part, left_firm, None)
        new_right_firm = Doubly_list(len_right_part, None, right_firm)
        new_left_firm.right_firm = new_right_firm
        new_right_firm.left_firm = new_left_firm
        if left_firm != None:
            left_firm.right_firm = new_left_firm
        if right_firm != None:
            right_firm.left_firm = new_right_firm
        now_firm = new_left_firm

    print(now_tax)

