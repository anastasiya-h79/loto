import loto_classes
import random

def choice_of_gamers(num_of_gamer):
    player = None
    while player not in ['c', 'h']:
        print(num_of_gamer, ' игроком будет человек или компьютер?')
        player = input('(c/h): ')
    if player == 'c':
        return loto_classes.Comp()
    return loto_classes.Gamer()

