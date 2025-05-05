# используем очередь из стандартной библиотеке
import queue

q = queue.Queue()
while 1:
    command = input().split()
    if command[0] == 'push':
        q.put(int(command[1]))
        print('ok')
    elif command[0] == 'pop':
        print(q.get() if not q.empty() else 'error')
    elif command[0] == 'front':
        print(q.queue[0] if not q.empty() else 'error')
    elif command[0] == 'size':
        print(q.qsize())
    elif command[0] == 'clear':
        q.queue.clear()
        print('ok')
    else:   # exit
        print('bye')
        break
