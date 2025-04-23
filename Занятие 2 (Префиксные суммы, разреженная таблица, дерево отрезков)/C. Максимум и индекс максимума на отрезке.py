# задача аналогична прошлой, только теперь нужно вывести и сам максимум
# просто немного изменяем прошлое решение
n = int(input())
nums = [[]]
nums[0] = list(map(lambda x: [int(x[1]), x[0]], enumerate(input().split(), 1)))
two_degree_j = 1
y = 1
while two_degree_j < len(nums[y-1]):
    nums.append([])
    for i in range(len(nums[y-1])-two_degree_j):
        nums[-1].append(max([nums[y-1][i], nums[y-1][i+two_degree_j]]))
    two_degree_j *= 2
    y += 1

degree_for_num = {}
degree = 0
two_degree_j = 1
for k in range(1,n+1):    # для каждой длины отрезка k считаем наибольше 2**j, так что 2**j <= k
    if k >= two_degree_j:
        degree += 1
        two_degree_j *= 2
    degree_for_num[k] = degree - 1

for _ in range(int(input())):
    l, r = map(int,input().split())
    print(*max([nums[degree_for_num[r - l + 1]][l - 1], nums[degree_for_num[r - l + 1]][r - 2 ** degree_for_num[r - l + 1]]]))
