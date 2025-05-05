import sys
sys.setrecursionlimit(10**9)

n = int(input())
links = [set() for _ in range(n+1)]
for _ in range(n-1):
    num1, num2 = list(map(int, input().split()))
    links[num1].add(num2)
    links[num2].add(num1)

def get_depth(prev_node, now_node):
    childs = 0
    for node in links[now_node]:
        if node != prev_node and now_node != node:
            childs += get_depth(now_node, node)
    answer[now_node] = childs + 1
    return childs + 1

answer = {1:n}
get_depth(0, 1)
print(*[el[1] for el in sorted(answer.items())])