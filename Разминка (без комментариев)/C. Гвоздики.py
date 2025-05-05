n = int(input())
coors = sorted(list(map(int, input().split())))
dp = [0, coors[1] - coors[0]]
if n>=3:
    dp.append(dp[-1] + (coors[2]-coors[1]))
    for i in range(3, n):
        dp.append(min(dp[-1], dp[-2]) + (coors[i] - coors[i-1]))
print(dp[-1])