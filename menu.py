import loto_classes
from loto_functions import choice_of_gamers
from random import randint, shuffle, sample


print('Добро пожаловать в игру ЛОТО!')
count_of_gamers = int(input('Введите число игроков: '))
gamers = []
for i in range(count_of_gamers):
    gamer = choice_of_gamers(i + 1)
    gamers.append(gamer)
bag = loto_classes.Bag()
while bag.nums:
    num = bag.take_num()
    for i in range(count_of_gamers):
        if not isinstance(gamers[i], loto_classes.Looser):
            print('Ходит', i + 1, ' игрок.')
        if not gamers[i].cross_out(num):
            gamers[i] = loto_classes.Looser()
        #bag.stats()
        if gamers[i].is_winning():
            print('Поздравляем! Вы победили!')
            break
