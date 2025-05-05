# реализуем очередь с помощью ООП
class Node():
    def __init__(self, prev, num):
        self.prev = prev
        self.num = num

head = None # нужен для удаления из начала очереди
tail = None # нужен для добавления в конец очереди
len_queue = 0   # длина очереди
while 1:
    command = input().split()
    if command[0] == 'push':    # добавляем в конец очереди
        num = int(command[1])
        new_el = Node(None,num)
        if not head:    # если изначально нет элементов
            head = new_el
        if tail:
            tail.prev = new_el
        tail = new_el
        len_queue += 1
        print('ok')
    elif command[0] == 'pop':   # удаляем из начала очереди
        # print(q.get() if not q.empty() else 'error')
        if not len_queue:
            print('error')
        else:
            print(head.num)
            head = head.prev
            len_queue -= 1
    elif command[0] == 'front': # выводим первый элемент
        if not len_queue:
            print('error')
        else:
            print(head.num)
    elif command[0] == 'size':
        print(len_queue)
    elif command[0] == 'clear':
        print('ok')
        head = None  # нужен для удаления из начала очереди
        tail = None  # нужен для добавления в конец очереди
        len_queue = 0  # длина очереди
    else:   # exit
        print('bye')
        break
