from random import randint


random_number = randint(1,101)
print('Угадайте число от 1 до 100')

while True:
    player_number = int(input())
    if player_number > random_number:
        print('Ваше число больше того, что загадано')
    elif player_number < random_number:
        print('Ваше число меньше того, что загадано')
    elif player_number == random_number:
        print('Отличная интуиция! Вы угадали число :)')    
     

