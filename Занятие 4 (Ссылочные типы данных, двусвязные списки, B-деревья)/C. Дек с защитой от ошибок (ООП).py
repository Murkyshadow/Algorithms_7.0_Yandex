# реализуем дек с помощью ООП

class Node():
    def __init__(self, prev, next, num):
        self.prev = prev
        self.next = next
        self.num = num

head = None
tail = None
len_queue = 0
while 1:
    command = input().split()
    if command[0] == 'push_back':      # добавляем в конец дека
        num = int(command[1])
        new_el = Node(None,tail,num)
        if not head:    # если изначально нет элементов
            head = new_el
        if tail:
            tail.prev = new_el
        tail = new_el
        len_queue += 1
        print('ok')
    elif command[0] == 'push_front':      # добавляем в начало дека
        num = int(command[1])
        new_el = Node(head,None,num)
        if not tail:    # если изначально нет элементов
            tail = new_el
        if head:
            head.next = new_el
        head = new_el
        len_queue += 1
        print('ok')
    elif command[0] == 'pop_back':   # удаляем из конца дека
        if not len_queue:
            print('error')
        else:
            print(tail.num)
            tail = tail.next
            if tail:
                tail.prev = None
            else:
                head = None # удалили последний эл значит и голова изменилась
            len_queue -= 1
    elif command[0] == 'pop_front':   # удаляем из начала дека
        if not len_queue:
            print('error')
        else:
            print(head.num)
            head = head.prev
            if head:
                head.next = None
            else:
                tail = None # удалили последний эл значит и хвост изменился
            len_queue -= 1
    elif command[0] == 'front': # выводим первый элемент
        if not len_queue:
            print('error')
        else:
            print(head.num)
    elif command[0] == 'back': # выводим последний элемент
        if not len_queue:
            print('error')
        else:
            print(tail.num)
    elif command[0] == 'size':
        print(len_queue)
    elif command[0] == 'clear':
        print('ok')
        head = None
        tail = None
        len_queue = 0  # длина очереди
    else:   # exit
        print('bye')
        break
