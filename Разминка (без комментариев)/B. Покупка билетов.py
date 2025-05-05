n = int(input())
customers = [n]
for _ in range(n):
    customers.append(list(map(int, input().split())))

best_cost_dp = [0, customers[1][0]]
for i in range(2, n+1):
    cost_for_1_customer = customers[i][0] + best_cost_dp[i-1]
    cost_for_2_customer = customers[i-1][1] + best_cost_dp[i-2]
    if i >= 3:
        cost_for_3_customer = customers[i-2][2] + best_cost_dp[i-3]
        best_cost_dp.append(min([cost_for_1_customer, cost_for_2_customer, cost_for_3_customer]))
    else:
        best_cost_dp.append(min([cost_for_1_customer, cost_for_2_customer]))
print(best_cost_dp[-1])