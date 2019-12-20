import random


class Card:

    def __init__(self):

        self.nums = []
        while len(self.nums) < 15:
            i = random.randrange(1, 91)
            if i not in self.nums:
                self.nums.append(i)

        self.strings = {}
        for i in range(3):
            self.strings[i] = self.nums[i * 5: i * 5 + 5]
            self.strings[i].sort()

        self.positions = []

    def make_card(self, num):

        print('Из мешка достали бочонок с числом: ', num)
        print('*' * 30)
        for i in range(3):
            for num in self.strings[i]:
                print(num, ' ', end=' ')
            print("\n")
        print("*" * 30)

    def __str__(self):
        return f'количество строк в карте {len(self.strings)}, количество номеров {len(self.nums)}'

    def __eq__(self, other):
        """
        сравниваем длину строк карточки
        """
        string01 = len(self.strings[0])
        string02 = len(self.strings[1])
        return string01 == string02

    def __ne__(self, other):
        """
        сравниваем длину и число строк (не нашла что еще можно сравнить в рамках имеющегося функционала))
        """
        numbers = len(self.nums)
        strings = len(self.strings)
        return len(self.nums) != len(self.strings)

    def __getitem__(self, item):
        """
        смотрим элементы карточки
        """
        return self.nums[item]



class Player:
    def __init__(self):
        self.card = Card()

    def is_winning(self):
        for i in range(3):
            if self.card.strings[i].count('-') < 5:
                return False
        return True

    def __str__(self):
        pass


class Comp(Player):

    def cross_out(self, num):

        self.card.make_card(num)
        if num in self.card.nums:
            for i in range(3):
                if num in self.card.strings[i]:
                    self.card.strings[i][self.card.strings[i].index(num)] = '-'
                    self.card.nums.pop(self.card.nums.index(num))
        return True

    def __str__(self):
        return f'Игрок компьютер - остались номера {self.card.nums}'

    def __eq__(self, other):
        """
        сравниваем число зачеркнутых номеров
        """
        strike01 = self.card.nums.count('-')
        strike02 = other.card.nums.count('-')
        return strike01 == strike02

    def __ne__(self, other):
        """
        сравниваем число зачеркнутых номеров
        """
        strike01 = self.card.nums.count('-')
        strike02 = other.card.nums.count('-')
        return strike01 != strike02


class Gamer(Player):

    def cross_out(self, num):

        self.card.make_card(num)
        answer = input('Проверьте, если число на Вашей карте. Зачеркнуть число? (y/n) ')
        if answer == 'y':
            if num not in self.card.nums:
                print('Сожалею! Такого числа нет на Вашей карте! Вы проиграли...')
                return False
            else:
                for i in range(3):
                    if num in self.card.strings[i]:
                        self.card.strings[i][self.card.strings[i].index(num)] = '-'
                        self.card.nums.pop(self.card.nums.index(num))
                    return True
        else:
            if num in self.card.nums:
                print('Сожалею! Такое число есть на Вашей карточке! Вы проиграли...')
                return False
            return True

    def __str__(self):
        return f'Игрок человек - осталось {len(self.card.nums)} номеров'

    def __eq__(self, other):
        """
        сравниваем число зачеркнутых номеров
        """
        strike01 = self.card.nums.count('-')
        strike02 = other.card.nums.count('-')
        return strike01 == strike02

    def __ne__(self, other):
        """
        сравниваем число зачеркнутых номеров
        """
        strike01 = self.card.nums.count('-')
        strike02 = other.card.nums.count('-')
        return strike01 != strike02


class Looser(Player):
    def cross_out(self, num):
        pass


class Bag:

    def __init__(self):
        self.nums = [i for i in range(1, 91)]
        self.winning_nums = []

    def take_num(self):
        return self.nums.pop(random.randrange(len(self.nums)))

    def __str__(self):
        return f'В бочонке осталось {len(self.nums)} номеров'

    def __eq__(self, other):
        return len(self.winning_nums) == len(other.winning_nums)


    if __name__ == '__main__':

        import unittest

        class TestCard(unittest.TestCase):

            def setUp(self):
                self.card = Card()

            def tearDown(self):
                pass

            def test_str(self):
                self.assertEqual(len(self.card.strings), 3)
                self.assertEqual(len(self.card.nums), 15)

            def test_eq(self):
                string01 = len(self.card.strings[0])
                string02 = len(self.card.strings[1])
                assert string01 == string02



