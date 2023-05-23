n = int(input("Введите любое число: "))
k = 0
while 2 ** k < n:
    print(2 ** k, end=' ')
    k += 1