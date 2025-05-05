# через список по мне так реализовать легче, чем через ООП
# просто в списке храним по 4 числа [рейтинг, индекс предыдущего игрока, индекс следующего игрока, индекс текущего игрока]
# в 1ом раунде проходимся по всем игрокам и находим выбывших, выбывших вычеркиваем (просто обнавляем индексы след. и пред.)
# во втором и след. раундах проходимся только по соседям выбывших (тк у других соседи не менялись и они 100% остануться, если не выбыли в 1ом раунде)

n = int(input())
count_active_players = n    # кол-во не выбывших игроков
players = list(map(lambda indNow_rating: {'rating':int(indNow_rating[1]), 'ind_prev_player':indNow_rating[0]-1,'ind_next_player':indNow_rating[0]+1, 'ind_now_player':indNow_rating[0]}, enumerate(input().split())))
players[0]['ind_prev_player'] = count_active_players-1  # у первого игрока предыдущим является последний
players[-1]['ind_next_player'] = 0  # у последнего игрока следующим является первый

start_player = players[0]   # в целом любой не выбывший игрок, с которого мы будем начинать проверка по кругу
players_lastRaound = [0]*n  # наш ответ: для каждого игрока запоминаем в каком раунде выбыл
players_for_check = players # игроков, которых надо проверить на предмет выбывания (изначально всех)
for num_round in range(1, n):
    ind_losing_players = set() # индексы игроков, которые выбыли в данном раунде
    for now_player in players_for_check:   # проверяем каждого игрока на предмет выбывания из игры
        if players[now_player['ind_prev_player']]['rating'] > now_player['rating'] and players[now_player['ind_next_player']]['rating'] > now_player['rating']: # если рейтинг предыдущего и следующего больше текущего, то он выбывает
            ind_losing_players.add(now_player['ind_now_player'])

    if len(ind_losing_players) == 0 or count_active_players == 2:    # нет выбывших или осталось 2 игрока
        break
    count_active_players -= len(ind_losing_players)
    players_for_check = []
    for ind_player in ind_losing_players:   # вычеркиваем выбывших игроков
        players_lastRaound[ind_player] = num_round
        now_player = players[ind_player]
        prev_player = players[now_player['ind_prev_player']]
        next_player = players[now_player['ind_next_player']]
        prev_player['ind_next_player'] = next_player['ind_now_player']
        next_player['ind_prev_player'] = prev_player['ind_now_player']
        # players_for_check.append(prev_player)   # есть смысл проверять только соседий выбывших игроков, тк у тех у кого не поменялись соседи не проиграют в этом раунде
        # players_for_check.append(next_player)   # а те у кого появились новые соседи могут вылететь из игры
        players_for_check.append(prev_player if prev_player['rating'] < next_player['rating'] else next_player)  # вообще из 2x соседей есть шанс вылетить только у меньшего
print(*players_lastRaound)