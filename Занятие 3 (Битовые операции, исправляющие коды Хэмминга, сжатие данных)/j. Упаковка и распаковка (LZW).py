# 7:55- 9 :50 11:30 - 12:34 12:55-16:05 16:30-17:55 0:41-2:04
# использовал алгоритм LZW, для букв отводил 5 бит, а для номеров постепенно увеличивал кол-во бит
# в зависимости от длины словаря
# только python (не pypy)!

def pack(s):
    """
    преобразуем строку в запакованный вид
    :param s: исходная строка
    :return: массив с запакованной строкой
    """
    word_num = {'':0}   # {слово:номер}
    new_word = ''
    pack_str = [] # [предыдущий номер слова; символ, который добавился; ну и еще сохраняем кол-во бит для номера]
    prev_num = 0
    now_bit_for_num = 2 # кол-во байт нужное для зашифровки максимального слова, изначально - 2 бита и с разростанием словаря увеличиваем кол-во бит
    for sym in s:
        new_word += sym
        if new_word in word_num:
            prev_num = word_num[new_word]
        else:
            if 2**now_bit_for_num == len(word_num) + 1:
                now_bit_for_num += 1
            word_num[new_word] = len(word_num)
            pack_str.append([prev_num, sym, now_bit_for_num])
            prev_num = 0
            new_word = ''

    if new_word != '':
        if 2**now_bit_for_num == len(word_num) + 1:
            now_bit_for_num += 1
        pack_str.append([prev_num, '', now_bit_for_num])

    return pack_str

def pack_str_to_nums(pack_str):
    """
    запакованную строку преобразует в двоичную строку, а затем в десятичные числа
    :param pack_str: запакованная строка
    :return: десятичные числа
    """
    sym_to_num = {sym : (bin(31-i)[2:]) for i, sym in enumerate('abcdefghijklmnopqrstuvwxyz')}  # тк мы знаем, что в тексте будут только буквы, то присваиваем каждой из 26 букв номер (выделяя не больше 5 бит)
    res_bin = ''
    for num, sym, now_bite in pack_str: # создаем двоичную строку из 'номера пред эл.' + 'добавленного символа'
        bin_num = bin(num)[2:]
        bin_num = '0'*(now_bite - len(bin_num)) + bin_num
        if sym != '':
            bin_sym = '0'*(5-len(sym_to_num[sym])) + (sym_to_num[sym])
        else:
            bin_sym = '00000'   # если нет последнего символа (в конце строки)
        res_bin += (bin_num + bin_sym)

    if len(res_bin) % 8 != 0:   # округляем кол-во бит до целого кол-ва байт
        res_bin += '0' * (8 - (len(res_bin) % 8))
    i = 0
    output_nums = []
    while i < len(res_bin): # двоичную строку нарезаем по 8 бит и превращаем в числа
        num = int(res_bin[i:i+8], 2)
        output_nums.append(num)
        i += 8
    return output_nums

def unpack(nums):
    """
    превращает десятичные числа обратно в текст
    сначала превращает десятичные числа в двоичную строку,
    а потом считывает пары: номер пред. эл + добавленный символ
    :param nums: десятичные числа
    :return: исходная строка букв
    """
    res_bin = ''
    for num in nums:
        bin_num = bin(num)[2:]
        bin_num = '0' * (8 - len(bin_num)) + bin_num
        res_bin += bin_num

    num_to_sym = {31-i:sym for i, sym in enumerate('abcdefghijklmnopqrstuvwxyz')}
    num_to_sym[0] = ''
    word_num = {0: ''}
    unpack_str = ''
    now_bit_for_num = 2 # кол-во бит для кодировки номера числа
    now_ind = 0
    while now_ind+now_bit_for_num <= len(res_bin):
        prev_num = int(res_bin[now_ind:now_ind+now_bit_for_num], 2)
        now_ind += now_bit_for_num
        sym = num_to_sym[int(res_bin[now_ind:now_ind+5], 2)]
        now_ind += 5  # бит в символе
        word_num[len(word_num)] = word_num[prev_num] + sym  # новое слово
        unpack_str += word_num[prev_num] + sym
        if 2**now_bit_for_num == len(word_num) + 1:
            now_bit_for_num += 1

    return unpack_str

type = input()
if type == 'pack':
    s = input()
    pack_str = pack(s)
    nums = pack_str_to_nums(pack_str)   # упаковонное переводим в числа
    print(len(nums))
    # while len(nums) > len(s)/2: # проверка, если по длине не совпадает, то тестирующая система выдаст TL
    #     pass
    # print(f'сжато до {len(nums)} байт, {len(nums)/len(s)}% от изначального размера')
    print(*nums,  flush=True)
else:
    n = int(input())
    nums = list(map(int, input().split()))
    unpack_str = unpack(nums)
    print(unpack_str,  flush=True)