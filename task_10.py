import random

n = int(input("Введите количество монет: "))
count_zero = 0
count_one = 0
if n > 10:
    for i in range(n):
        i = random.randrange(2)
        if i == 0:
            count_zero += 1
        else:
            count_one += 1
else:
    while count_zero + count_one != n:
        coin = int(input("Введите '1' если монетка выпала орлом, и '0' если решкой "))
        if coin == 1:
            count_one += 1
        else:
            count_zero += 1
print('На столе',count_zero, 'монет решкой и', count_one, 'монет орлом,', end=' ')
if count_zero > count_one:
    print(f'минимум нужно превернуть {count_one} монет, чтобы все стали одной стороной')
else:
    print(f'минимум нужно превернуть {count_zero} монет, чтобы все стали одной стороной')


