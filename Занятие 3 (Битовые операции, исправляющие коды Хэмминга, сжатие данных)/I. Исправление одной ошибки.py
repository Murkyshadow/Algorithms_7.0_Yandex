# 18:17 - 19:11 20:34-22:27
# ну, тут стандартно, как было в лекции с помощью алгоритма Хэмминга: делаем доп. биты, чтобы было нечетное кол-во единиц
# и при поиске сломанного бита с помощью доп. битов находим
# разряды (где оказалось четное кол-во единиц) и по разрядам получаем число - номер сломанного бита

def counter_number_of_unit(s):
    """
    считаем единицы в step разрядах черех step, потом в step*2 разрядах черех step*2 разрядов,
    затем в  в step*4 разрядах черех step*4 и тд
    :param s: список с разрядами
    """
    step = 1  # считаем единицы в 1ом разряде, 1 пропускаем до конца строки, потом увеличиваем шаг и считаем единицы в 2x разрядах, 2 пропускаем, затем в 4х, 8ми и тд
    units = [] # наши насчитанные единицы
    while step < len(s):
        now_ind = step - 1
        count_unit = 0
        while now_ind < len(s):  # насчитываем единицы с опред. шагом
            for i in range(now_ind, min(len(s), now_ind + step)):
                if s[i] == '1':
                    count_unit += 1
            now_ind = (i + 1) + step  # пропускаем step разрядов
        units.append(count_unit)
        step *= 2
    return units

def get_str_with_extra_bits(s_bin):
    """
    добавляем доп. биты в исходную строку
    :param s_bin: исходная строка
    :return: строка с доп. битами (в виде списка)
    """
    ind_extra_bits = set(2**degree-1 for degree in range(17+1))  # индексы доп. бит, для входных данных в 100к будет всего 17 доп. бит (это можно понять если посмотре на ограничение выходной строки в не более 100017)
    new_s = [None]
    for ind_original_str, bit in enumerate(s_bin):
        if len(new_s) in ind_extra_bits:    # если индекс новго элемента будет индексом доп. эл, то добавляем None
            new_s.append(None)  # мы пока не знаем какой индекс добавить
        new_s.append(bit)

    units = counter_number_of_unit(new_s)
    for degree in range(len(units)):
        if units[degree] % 2 == 0:  # если четное кол-во единиц
            new_s[2**degree-1] = '1'    # тогда доп бит будет единицей (чтобы было нечетное кол-во) - step-1 - это ind доп бита
        else:
            new_s[2**degree-1] = '0'

    return new_s

def get_normal_str(wrong_bin_str):
    """
    ищет номер сломанного бита и исправляет ошибку, исходную строку бит
    :param wrong_bin_str: строка со сломанным битом
    :return: исходная строка - в виде списка
    """
    wrong_bin_str = list(wrong_bin_str)
    num_wrong_bit = 0   # номер сломанного бита
    units = counter_number_of_unit(wrong_bin_str)
    for degree, num_units in enumerate(units):  # ищем номер млованного бита
        if num_units % 2 != 1:  # должно быть нечетное кол-во единиц, если четное, то какой-то бит сломан и разряд в номере сломанного бита = единице
            num_wrong_bit += 2 ** degree

    if num_wrong_bit - 1 != -1: # заменяем сломанный бит на отрицательный, если -1, то сломанных бит нет
        wrong_bin_str[num_wrong_bit - 1] = str(int(not int(wrong_bin_str[num_wrong_bit - 1])))  # при not int(s_bin[wrong_bit - 1]) получем True или False, int(True или False) = 1 или 0 и в строку

    good_str = ''
    two_in_degree = 1

    for i in range(len(wrong_bin_str)): # создаем иходную строку без доп.бит
        if i == two_in_degree - 1:  # пропускаем доп. биты
            two_in_degree *= 2
        else:
            good_str += wrong_bin_str[i]
    return good_str

type_operation = int(input())
if type_operation == 1: # добавляем доп. биты
    s_bin = input()
    print(*get_str_with_extra_bits(s_bin), sep="")
else:   # ищем сломанный бит
    s_bin_hamming = input()
    print(get_normal_str(s_bin_hamming))

# Тестик:
# 1
# 0100010000111101  - ввод
# 010010010100001111101 - вывод
# 2
# 000010010100001111101 - ввод со сломанным битом (к примеру 2ой)
# 0100010000111101 - вывод (исходная строка)

