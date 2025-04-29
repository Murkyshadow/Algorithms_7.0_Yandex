import unittest
from unittest import TestCase
import J
from time import *
from random import randint

class Timer():
    def __init__(self):
        self.st = time()

    def end(self):
        return time()-self.st

class Test(TestCase):
    def test_defult(self):
        ans = J.solution(5,3, ['Cappuccino 25','Car 5','Food 4','Apartment 1','Shopping 7'])
        self.assertEqual(ans, [4,9,['Apartment','Car','Food','Shopping']])

    def test_one_good(self):
        ans = J.solution(1, 3, ['Cappuccino 3'])
        self.assertEqual(ans, [1, 1, ['Cappuccino']])

    def test_one_bad(self):
        ans = J.solution(1, 1, ['Cappuccino 2'])
        self.assertEqual(ans, [0, 0, []])

    def test_sort(self):
        ans = J.solution(3, 1, ['b 1', 'a 3', 'c 1'])
        self.assertEqual(ans, [3, 5, ['a', 'b', 'c']])

    def test_any_1(self):
        ans = J.solution(2, 1, ['a 3','b 1'])
        self.assertEqual(ans, [1, 1, ['b']])

    def test_any_2(self):
        ans = J.solution(2, 1, ['a 3','b 2'])
        self.assertEqual(ans, [0, 0, []])

    def test_any_3(self):
        ans = J.solution(3, 1, ['a 3','b 2', 'c 100'])
        self.assertEqual(ans, [0, 0, []])

    def test_any_4(self):
        ans = J.solution(3, 1, ['a 1','b 2','c 3'])
        self.assertEqual(ans, [3, 6, ['a', 'b', 'c']])

    def test_any_4_5(self):
        ans = J.solution(3, 2, ['a 1','b 2','c 5'])
        self.assertEqual(ans, [3, 5, ['a', 'b', 'c']])

    def test_any_5(self):
        ans = J.solution(3, 1, ['a 1','b 1','c 1'])
        self.assertEqual(ans, [3, 3, ['a', 'b', 'c']])

    def test_choice_days(self):
        ans = J.solution(5, 1, ['b 1', 'a 3', 'c 1', 'd 2', 'e 132'])
        self.assertEqual(ans, [4, 7, ['a', 'b', 'c', 'd']])

    def test_time_limit(self):
        n = randint(990, 1000)
        data = [str(s) + ' ' + str(randint(1, 1000)) for s in range(n)]
        t = Timer()
        ans = J.solution(n, randint(1, 10000), data)
        print(t.end())
        self.assertTrue(t.end() <= 2) # для pypy и 2 сойдет

    def test_any_6(self):
        ans = J.solution(4, 2, ['a 1','b 2','c 5', 'd 7'])
        self.assertEqual(ans, [4, 9, ['a', 'b', 'c', 'd']])


    def test_any_7(self):
        ans = J.solution(11, 2,['Car1 1','Car2 1','Car3 2','Car4 3','Car5 7','Car6 7','Car7 7','Car8 8','Car9 8','Car10 8','Car 45'])
        self.assertEqual(ans, [11, 59, ['Car','Car1', 'Car10', 'Car2', 'Car3', 'Car4','Car5', 'Car6', 'Car7', 'Car8', 'Car9']])


    def test_similar_title(self):
        ans = J.solution(11, 2, ['Car 1', 'Car2 1', 'Car 2', 'Car2 3', 'Car 7', 'Car2 7', 'Car2 7', 'Car2 8', 'Car 8', 'Car 8', 'Car2 45'])
        self.assertEqual(ans, [11, 59, ['Car']*5+['Car2']*6])


if __name__ == '__main__':
    unittest.main()
