# алгоритм поиска
from random import randint

x = randint(0, 100000000)  # рандомное число от 0 до 100

# print('Загаданное число было', x, 'и для его поиска перебором потребовалось', count_perebor, 'итераций методом 1')
#
# count_random = 0
# # метод случайного отгадывания
# y = randint(0, 100)
# while x != y:
#     y = randint(0, 100)
#     count_random += 1
#
# print('Загаданное число было', x, 'и для его поиска перебором потребовалось', count_random, 'итераций методом 1')
#
# count_bin = 1
# y = int(input('Давай начнем игру - угадай число от 0 до 100: '))
# while x != y:
#     if x < y:
#         print('Меньше ')
#     else:
#         print('больше ')
#     y = int(input('Введите число'))
#     count_bin += 1
# print('Загаданное число было', x, 'и для его поиска бинарным алгоритмом потребовалось', count_bin, 'итераций методом 1')
#########################


count_bin = 1
# y = int(input('Давай начнем игру - угадай число от 0 до 100: '))
left = 0
right = 1000000000
mid = 0

while x != mid:
    mid = (right + left) // 2
    print(left, right)
    if x < mid:
        print('Меньше ')
        right = mid - 1
    else:
        print('больше ')
        left = mid + 1
    # y = int(input('Введите число'))
    count_bin += 1
print('Загаданное число было', x, 'и для его поиска бинарным алгоритмом потребовалось', count_bin, 'итераций методом 1')