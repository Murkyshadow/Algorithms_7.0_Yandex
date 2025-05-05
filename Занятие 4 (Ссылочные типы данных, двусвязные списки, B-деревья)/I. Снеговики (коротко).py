# кто-то написал, что у него код в 5 строк... ну, а я что хуже?
snowman_clones = [[0,None]]    # [mass, prev]
for _ in range(int(input())):
    num_snowman, add_mass = map(int, input().split())
    snowman_clones.append([snowman_clones[num_snowman][0] + add_mass if add_mass != 0 else snowman_clones[snowman_clones[num_snowman][1]][0], num_snowman if add_mass != 0 else snowman_clones[snowman_clones[num_snowman][1]][1]])
print(sum([mass for mass,prev in snowman_clones]))

# а дальше если еще for в одну строку использовать... то получаем 3 строки (по памяти уложился тютилюка в тютельку 63.94Mb)! (тут еще можно создать список с массами каждого снеговика, использовать sum и рсазу печатать и уложиться в 2 строки, но по памяти не прошло)
snowman_clones = [[0,None]]    # [mass, prev]
for num_snowman, add_mass in [list(map(int, input().split())) for _ in range(int(input()))]: snowman_clones.append([snowman_clones[num_snowman][0] + add_mass if add_mass != 0 else snowman_clones[snowman_clones[num_snowman][1]][0], num_snowman if add_mass != 0 else snowman_clones[snowman_clones[num_snowman][1]][1]])
print(sum([mass for mass,prev in snowman_clones]))

# а теперь используем грязный хак и пишем все в одну строку
exec("""snowman_clones, mass_snowmen = [[0,None]], 0\nfor _ in range(int(input())):\n\tnum_snowman, add_mass = map(int, input().split())\n\tsnowman_clones.append([snowman_clones[num_snowman][0] + add_mass if add_mass != 0 else snowman_clones[snowman_clones[num_snowman][1]][0], num_snowman if add_mass != 0 else snowman_clones[snowman_clones[num_snowman][1]][1]])\nprint(sum([mass for mass,prev in snowman_clones]))""")
# на самом деле с помощью exec можно почти любой код уместить в одну строчку, но по настоящему он удобен, когда дается строка с каким-то примером по типу: "1+  3* 32 / 2 - (-1000)**2"
