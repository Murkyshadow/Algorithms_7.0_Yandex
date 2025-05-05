count_last_0, count_last_one_1, count_last_two_1 = 1, 1, 0
answer = 2
for now_len in range(1,int(input())):
    new_answer = answer*2 - count_last_two_1
    count_last_two_1, count_last_one_1, count_last_0 = count_last_one_1, count_last_0, answer
    answer = new_answer
print(answer)