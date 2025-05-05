# используем персистентность и будем хранить не всего снеговика
# каждый клон снеговика - это прошлый снеговик с добавленным шаром
# если же нужно убрать шар - то новым снеговиком станет прошлая версия прошлого снеговика
# (то есть прошлая версия без шара - это позапрошлая версия)
# то есть в новой верссии снеговика нужно хранить прошлую версию снеговика и его текущую массу

class snowman():
    def __init__(self, m, prev):
        self.mass_snowman = m
        self.prev_snowman = prev

snowman_clones = [snowman(0, None)] # изначально имеем снеговика с нулевой массой

n = int(input())
mass_snowmen = 0    # для ответа считаем массу всех снеговиков
for _ in range(n):
    num_snowman, add_mass = map(int, input().split())
    if add_mass != 0:   # добавляем шар
        new_mass = snowman_clones[num_snowman].mass_snowman + add_mass  # новая масса = массе клонированного снеговика + вес добавленного шара
        snowman_clones.append(snowman(new_mass, snowman_clones[num_snowman]))   # получаем нового снеговика с новой массой и делаем ссылку на предка снеговика (снеговик, которого клонировали)
    else: # = 0 удалить ласт шар
        new_mass = snowman_clones[num_snowman].prev_snowman.mass_snowman    # если удалить последний шар, то мы получим снеговика с массой снеговика, который был до него
        snowman_clones.append(snowman_clones[num_snowman].prev_snowman)     # по факту тут не получаем новго сснеговика, а откатываемся к предыдущему снеговику
    mass_snowmen += new_mass
print(mass_snowmen)