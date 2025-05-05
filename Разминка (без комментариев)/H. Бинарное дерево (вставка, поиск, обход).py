import sys
sys.setrecursionlimit(100000)

def add(num):
    now_el = tree
    while now_el != []:
        if num > now_el[0]:
            now_el = now_el[2]
        elif num < now_el[0]:
            now_el = now_el[1]
        else:    # равен
            return 'ALREADY'

    if now_el == []:
        now_el.extend([num, [], []])
        return 'DONE'


def search(num):
    now_el = tree
    while now_el != []:
        if num > now_el[0]:
            now_el = now_el[2]
        elif num < now_el[0]:
            now_el = now_el[1]
        else:  # равен
            return 'YES'
    return 'NO'

def printTree(tree, deaph):
    if tree[1] != []:
        printTree(tree[1], deaph+1)
    print('.'*deaph, tree[0], sep='')
    if tree[2] != []:
        printTree(tree[2], deaph + 1)

global tree
tree = []

while 1:
    try:
        command = input().split(" ")
        if command[0] == 'ADD':
            print(add(int(command[1])))
        elif command[0] == 'SEARCH':
            print(search(int(command[1])))
        else:
            printTree(tree, 0)
    except Exception:
        break