# идем по числам запоминаем минимальное число в данной последовательности и жадно выбираем максимум чисел
# (кол-во чисел не превышает минимума)
def solution(nums):
    ans = []
    now_len = 0
    now_min = nums[0]
    for num in nums:
        if num < now_min:
            now_min = num
            if num < now_len + 1:
                ans.append(now_len)
                now_len = 1
            else:
                now_len += 1
        elif now_min >= now_len + 1:
            now_len += 1
        else:
            now_min = num
            ans.append(now_len)
            now_len = 1
    ans.append(now_len)

    print(len(ans))
    print(*ans)

t = int(input())
for _ in range(t):
    n = input()
    solution(list(map(int, input().split())))

