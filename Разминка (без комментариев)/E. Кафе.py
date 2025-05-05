from math import inf

n = int(input())
costs =[0] + [int(input()) for _ in range(n)]
dp_matrix = [[inf]*(n+1) for _ in range(n+3)]
dp_matrix[1][0] = 0
max_tickets = 0

for x in range(1,n+1):
    max_tickets += (costs[x] >= 101)
    for y in range(1, max_tickets+2):
        if costs[x] >= 101:
            dp_matrix[y][x] = min(dp_matrix[y-1][x-1]+costs[x], dp_matrix[y+1][x-1])
        else:
            dp_matrix[y][x] = min(dp_matrix[y][x-1]+costs[x], dp_matrix[y+1][x-1])

ind_min_cost, min_cost =  min(enumerate(dp_matrix), key=lambda x: [x[1][-1],-x[0]]) # самая сложная строка в коде. Тут возвращается индекс и минимум по последнему столбцу и по макимальному индексу, если несколько одинаковых сумм (вместо максимума поставил знак минуса и получилось, что максимальный индекс станет минимальным)
print(dp_matrix[ind_min_cost][-1])
lost_tickets = ind_min_cost-1

days_use_ticket = []
for num_day in range(n, 1, -1):
    if dp_matrix[ind_min_cost+1][num_day-1] == dp_matrix[ind_min_cost][num_day] and costs[num_day] != 0:
        days_use_ticket.append(num_day)
        ind_min_cost += 1
    else:
        if costs[num_day] >= 101:
            ind_min_cost -= 1

print(lost_tickets, len(days_use_ticket))
print(*days_use_ticket[::-1])