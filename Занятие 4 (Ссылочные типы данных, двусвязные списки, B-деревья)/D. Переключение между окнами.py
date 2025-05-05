# реализуем односвязный список, в котором будем хранить наши окна
class window():
    def __init__(self, title, next):
        self.next_window = next # ссылка на след. окно
        self.title = title

count_windows = 0
active_win = None
for _ in range(int(input())):
    com = input()
    if com[:3] == 'Run':
        count_windows += 1  # новое окно
        new_win_title = com[4:]
        prev_win = active_win   # сохраняем предыдущее окно
        active_win = window(new_win_title, prev_win)  # предыдущее окно становится активным
    else: # alt+tab....
        count_tab = com.count('Tab')    # считаем сколько раз нажали Tab (так же можно посчитать кол-во "+")
        count_tab %= count_windows  # избавляем от цикличности
        now_win = active_win
        prev_win = None
        for _ in range(count_tab):  # идем до окна которое станет активным
            prev_win = now_win
            now_win = now_win.next_window
        if count_tab != 0:  # в случае если alt без tab или сделали целый круг с помощью tab
            prev_win.next_window = now_win.next_window  # предыдущее за выбранным начинает ссылаться на следующее за выбранным
            now_win.next_window = active_win    # выбранное будет ссылаться на текущее активное
            active_win = now_win    # и выбранное окно становится активным
    print(active_win.title)

