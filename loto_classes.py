"""
примеры возможных классов:
"""

import random


class Card:

    def __init__(self):
        """
        Описываем объект число
        """
        self.nums = []
        while len(self.nums) < 15:
            i = random.randrange(1, 91)
            if i not in self.nums:
                self.nums.append(i)
        """
        Описываем объект строка
        """
        self.strings = {}
        for i in range(3):
            self.strings[i] = self.nums[i * 5: i * 5 + 5]
            self.strings[i].sort()
        """
        Описываем объект позиция
        """
        self.positions = []


    def make_card(self, num):
        """
        Рисуем карточку
        :param num:
        :return:
        """
        print('Из мешка достали бочонок с числом: ', num)
        print('*' * 30)
        for i in range(3):
            for num in self.strings[i]:
                print(num, ' ', end=' ')
            print("\n")
        print("*" * 30)


class Player:
    def __init__(self):
        self.card = Card()

    def is_winning(self):
        for i in range(3):
            if self.card.strings[i].count('-') < 5:
                return False
        return True


class Comp(Player):

    def __init__(self, name='Computer'):
        #self.name = name
        self.card = Card()


    def cross_out(self, num):
        """
        Компьютер получает карту, проверяет наличие номера
        :param num:
        :return:
        """
        self.card.make_card(num)
        if num in self.card.nums:
            for i in range(3):
                if num in self.card.strings[i]:
                    self.card.strings[i][self.card.strings[i].index(num)] = '-'
                    self.card.nums.pop(self.card.nums.index(num))
            return True

    #def stats(self):
        #print(f'{self.name}. Осталось {len(self.compnums)} чисел : {self.compnums}')


class Gamer(Player):

    def __init__(self, name='Gamer'):
        #self.name = name
        self.card = Card()
        #self.nums = self.nums.copy()

    def cross_out(self, num):
        """
        Игорок получает карту, проверяет наличие номера
        :param num:
        :return:
        """
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
    #def stats(self):
        #print(f'{self.name}. Осталось {len(self.nums)} чисел : {self.nums}')


class Looser(Player):
    def cross_out(self, num):
        pass


class Bag:
    """
    Мешок с номерами
    """
    def __init__(self):
        self.nums = [i for i in range(1, 91)]

    def take_num(self):
        return self.nums.pop(random.randrange(len(self.nums)))        #list.pop([i]) - Возвращает элемент [на указанной позиции], удаляя его из списка

    def stats(self):
       print(f'В мешке {len(self.nums)} боченков.')