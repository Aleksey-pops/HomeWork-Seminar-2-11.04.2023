# Задача 10: На столе лежат n монеток.
# Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
from random import randint

n = int(input('Введите количество монет которые находятся на столе: '))
count1 = 0
count2 = 0
for i in range(n):
    x = randint(0, 1)
    if x == 0:
        count1 += 1
    else:
        count2 += 1
if n < 2:
    print('Мало монет монет!!! ')
elif count1 > count2:
    print('Число монет с орлом', (count2),
          'меньше, их нужно перевернуть, а число монет с решкой', count1)
elif count1 < count2:
    print('Число монет с решкой', count1,' меньше, их нужно перевернуть а число монет с орлом', count2)
else:
    print('Количество монет равно межно перевернуть монеты слюбой стороной!')
