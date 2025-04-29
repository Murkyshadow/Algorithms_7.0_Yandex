# жадно выбираем для каждой группы минимальную подходящую аудиторию (для этого отсортируем аудитории и идем по ним слева направо)
n, m = map(int, input().split())
groups = sorted([[stud, i] for i, stud in enumerate(list(map(int, input().split())))], reverse= True)
auditoriums = sorted([[comp, i] for i, comp in enumerate(list(map(int, input().split())))], reverse= True)

answer = [0]*n
count_use_auditorium = 0
now_auditorium = 0
now_group = 0

while now_group < len(groups) and now_auditorium < len(auditoriums):
    if auditoriums[now_auditorium][0] > groups[now_group][0]:
        answer[groups[now_group][1]] = auditoriums[now_auditorium][1]+1
        now_auditorium += 1
        count_use_auditorium += 1
    now_group += 1

print(count_use_auditorium, *answer, sep='\n')