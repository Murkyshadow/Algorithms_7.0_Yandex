# генератор строк для отладки рвашего решения
import random
import math

def get_str_with_extra_bits(s):
    """получаем строку с доп битами"""
    pass

def get_normal_str(s):
    """получаем исходную строку"""
    pass

while 1:
    n = random.randint(10, 30)
    s = [str(random.randint(0,1)) for _ in range(n)]
    s_bin = ''.join(s)  # сгенерированная строка
    s_bin_hamming = list(get_str_with_extra_bits(s_bin))
    i = random.randint(0, len(s_bin_hamming) - 1)  # выбираем бит для замены
    new_el = str(random.randint(0,1))   # выбираем на что его заменить
    s_bin_hamming[i] = new_el            # заменяем

    s_good = get_normal_str(''.join(s_bin_hamming))
    if s_bin != s_good:
        print(s_bin)
        print(f'er ind {i} на {new_el}', s_bin)
    if math.ceil(math.log(len(s), 2)) + len(s) < len(s_bin_hamming):
        print('слишком много бит в закодированной строке')

# Тестик:
# 1
# 0100010000111101  - ввод
# 010010010100001111101 - вывод
# 2
# 000010010100001111101 - ввод со сломанным битом (к примеру 2ой)
# 0100010000111101 - вывод (исходная строка)