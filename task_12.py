x_plus_y = int(input("Введите сумму двух чисел: "))
x_multiply_by_y = int(input("Введите произведение двух чисел: "))
for x in range(1001):
    for y in range(1001):
        if x + y == x_plus_y and x * y == x_multiply_by_y:
            print(x, y)
            exit()
print("Решения для этих пар чисел не существует")