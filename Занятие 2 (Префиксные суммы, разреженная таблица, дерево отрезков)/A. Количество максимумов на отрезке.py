import math

n = int(input())
len_nums = 1
while len_nums < n:
    len_nums *= 2

nums = [None]*(len_nums-1) + list(map(lambda x: [int(x), 1], input().split())) + [[-math.inf,-math.inf]]*(len_nums-n)
for ind in range(len(nums)-len_nums-1, 0-1, -1):
    ind_child_l = ind * 2 + 1
    ind_child_r = ind_child_l + 1
    count_max = 0
    count_max = max([nums[ind_child_l],nums[ind_child_r]])[1]
    if nums[ind_child_l][0] == nums[ind_child_r][0]:   # равно
        count_max = nums[ind_child_l][1] + nums[ind_child_r][1]
    nums[ind] = [max(nums[ind_child_l][0], nums[ind_child_r][0]), count_max]

def get_max(l, r, now_ind, left_section, right_section):
    if now_ind > len(nums)-1 or r < left_section or right_section < l:   # не пересекаются
        return [-math.inf, -math.inf]
    elif l <= left_section and r >= right_section:  # текущая секция полностью входит в ответ
        return nums[now_ind]
    else:   # частично входит
        ind_child_l = now_ind * 2 + 1
        max_l = get_max(l, r, ind_child_l, left_section, (left_section+right_section)//2)
        max_r = get_max(l, r, ind_child_l+1, (left_section+right_section)//2+1, right_section)
        if max_r[0] == max_l[0]:
            return [max_l[0], max_r[1] + max_l[1]]
        return max([max_r, max_l])

for _ in range(int(input())):
    left_ind, right_ind = map(int,input().split())
    print(*get_max(left_ind-1, right_ind-1, 0, 0, len_nums-1))
