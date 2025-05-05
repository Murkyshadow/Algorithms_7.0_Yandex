# без ООП (экономней по памяти, проходит на pypy)

n = int(input())
mass_snowmen =  0
snowman_clones_mass = [0]*(n+1)   # массы каждого снеговика
snowman_clones_prev = [0]*(n+1)   # индексы предыдущих снеговиков
for i in range(n):
    num_snowman, add_mass = map(int, input().split())
    mass_new_snowman = snowman_clones_mass[num_snowman] + add_mass if add_mass != 0 else snowman_clones_mass[snowman_clones_prev[num_snowman]]
    snowman_clones_mass[i+1] = mass_new_snowman
    mass_snowmen += mass_new_snowman
    snowman_clones_prev[i+1] = num_snowman if add_mass != 0 else snowman_clones_prev[snowman_clones_prev[num_snowman]]
print(mass_snowmen)
