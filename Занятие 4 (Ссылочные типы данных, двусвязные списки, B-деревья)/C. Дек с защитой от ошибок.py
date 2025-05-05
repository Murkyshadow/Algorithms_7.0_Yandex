# Используем дек из стандартной библиотеки
import collections

dq = collections.deque()

while 1:
    command = input().split()
    if command[0] == 'push_front':
        dq.appendleft(int(command[1]))
        print('ok')
    elif command[0] == 'push_back':
        dq.append(int(command[1]))
        print('ok')
    elif command[0] == 'pop_front':
        print(dq.popleft() if len(dq) != 0 else 'error')
    elif command[0] == 'pop_back':
        print(dq.pop() if len(dq) != 0 else 'error')
    elif command[0] == 'front':
        print(dq[0] if  len(dq) != 0 else 'error')
    elif command[0] == 'back':
        print(dq[-1] if len(dq) != 0 else 'error')
    elif command[0] == 'size':
        print(len(dq))
    elif command[0] == 'clear':
        dq = collections.deque()
        print('ok')
    else:   # exit
        print('bye')
        break
