n = int(input())
parent_child = {}
childs, parents = set(), set()
for _ in range(n-1):
    child, parent = input().split()
    childs.add(child)
    parents.add(parent)
    parent_child[parent] = parent_child.setdefault(parent, []) + [child]

start_parent = (parents - childs).pop()
stack_par = [start_parent]
answer = {start_parent:0}
while stack_par:
    for child in parent_child[stack_par[0]]:
        answer[child] = answer[stack_par[0]] + 1
        if child in parent_child:
            stack_par.append(child)
    stack_par.pop(0)

print(*[f"{name} {answer[name]}" for name in sorted(list(childs.union(parents)))], sep='\n')