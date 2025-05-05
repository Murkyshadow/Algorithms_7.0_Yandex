# стек на основе списка
stack = []
while 1:
    command = input().split()
    if command[0] == 'push':
        stack.append(int(command[1]))
        print('ok')
    elif command[0] == 'pop':
        print(stack.pop() if len(stack)!= 0 else 'error')
    elif command[0] == 'back':
        print(stack[-1] if len(stack)!= 0 else 'error')
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'clear':
        stack = []
        print('ok')
    else:   # exit
        print('bye')
        break
