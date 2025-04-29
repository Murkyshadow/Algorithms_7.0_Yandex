# сортируем по стоимости руб/за секунду, далле набираем этих карточек до максимума
# и в конце встатет выбор, взять еще одну такую карточек и добрать оставшееся
# кол-во секунд или же добрать кол-во секунд другими карточка, для этого рекурсивно находим
# минимаьльную стоимость для оставшегося времени при выходе из функции выбираем наименьшую стоимость
import math

limit = int(input())
times = list(map(int, input().split()))
costs = [2**exp for exp in range(31)]
rubs_per_sec = sorted([[costs[i]/times[i], i] for i in range(31)])

def get_best_cost(best_cost_lost_limit, lost_limit, i):
    if i > 30:
        return best_cost_lost_limit
    ind = rubs_per_sec[i][1]
    buy_cards = math.ceil(lost_limit / times[ind]) - 1
    new_best_cost_lost_limit = costs[ind]*buy_cards + get_best_cost(costs[ind], lost_limit - (buy_cards*times[ind]), i + 1)
    best_cost_lost_limit = min(best_cost_lost_limit, new_best_cost_lost_limit)
    return best_cost_lost_limit

print(get_best_cost(math.inf, limit, 0))