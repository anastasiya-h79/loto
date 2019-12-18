import random
import unittest

from loto_classes import Card, Player, Comp, Gamer, Bag


class TestCard(unittest.TestCase):

    def setUp(self):
        self.card = Card()

    def tearDown(self):
        pass

    def test_init(self):
        self.assertEqual(len(self.card.nums), 15)
        self.assertEqual(len(self.card.strings), 3)


    def test_make_card(self):
        self.assertEqual(len(self.card.strings), 3)


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.card = Card()

    def test_is_winning(self):
        self.assertEqual(len(self.card.strings), 3)
        self.assertTrue(self.card.strings, '-')


class TestComp(unittest.TestCase):

    def setUp(self):
        self.card = Card()

    def test_cross_out(self):
        self.assertTrue(self.card.strings, '-')


class TestGamer(unittest.TestCase):

    def setUp(self):
        self.card = Card()

    def test_cross_out(self):
        answer = ['y', 'n']
        self.assertEqual(answer, ['y', 'n'])
        num = random.randint(0, 90)
        while answer == 'y':
            self.assertIn(num, self.card.nums)
        while answer == 'n':
            self.assertNotIn(num, self.card.nums)


class TestBag(unittest.TestCase):

    def setUp(self):
        self.card = Card()

    def test_init(self):
        self.assertTrue(self.card.nums, [1, 91])

    def test_take_num(self):
        self.assertEqual(len(self.card.nums), 15)








