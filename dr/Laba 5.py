Kseniya, [20 марта 2024 г., 15: 31:0
8]:
from random import randint

n = int(input("Введите кол-во строк лабиринта -> "))
m = int(input("Введите кол-во столбцов лабиринта -> "))
print("Теперь вводите лабиринт")
print(".(точка) означает, что клетка пустая")
print("+(плюс) означает, что в этой клетке стена")

karta = []
for i in range(n):
    s = list(input("Введите строку -> "))
    karta.append(s)

# karta = [list("++.+"), list("...+"), list("+++.")]
main_x = randint(0, n - 1)
main_y = randint(0, m - 1)
while karta[main_x][main_y] == '+':
    main_x = randint(0, n - 1)
    main_y = randint(0, m - 1)

'''
++.+
...+
+++.
'''

if main_x == 0 or main_x == n - 1:
    karta[main_x][main_y] = '+'
if main_y == 0 or main_y == m - 1:
    karta[main_x][main_y] = '+'


def go(main_x, main_y, k_now):
    typik = False
    k = k_now
    x = main_x
    y = main_y
    while 0 < x < n - 1:
        k += 1
        if x - 1 >= 0 and karta[x - 1][y] == '.':
            x -= 1
            go(x, y, k)
        elif x + 1 < n and karta[x + 1][y] == '.':
            x += 1
            go(x, y, k)
        # Тупик
        else:
            typik = True
            break
    variants.append([typik, k, [x, y]])

    typik = False
    k = k_now
    x = main_x
    y = main_y
    while 0 < y < n - 1:
        k += 1
        if y - 1 >= 0 and karta[x][y - 1] == '.':
            y -= 1
            go(x, y, k)
        elif y + 1 < m and karta[x][y + 1] == '.':
            y += 1
            go(x, y, k)
        # Тупик
        else:
            typik = True
            break
    variants.append([typik, k, [x, y]])


main_x = 1
main_y = 2
variants = []
go(main_x, main_y, 0)

for i in range(len(variants)):
    print("Маршрут привел в ", variants[i][2][0] + 1, variants[i][2][1] + 1)

Kseniya, [20 марта 2024 г., 16: 20:04]:
from random import randint

n = int(input("Введите кол-во строк матрицы -> "))
m = int(input("Введите кол-во столбцов матрицы -> "))
matr = []
a = 10 * n
for i in range(n):
    b = a + m
    line = [randint(a, b)]
    for j in range(m - 1):
        value = randint(a, b)
        while value in line or value <= line[-1]:
            value = randint(a, b)
            if line[-1] == b:
                b += m
        line.append(value)
    matr.append(line)
    a += randint(b - a, m + (b - a))
print("Сформированная случайная матрица:")
for i in range(n):
    for j in range(m):
        print(matr[i][j], end=' ')
    print()
k = int(input("Введите число k, которое попытаемся найти в матрице -> "))

count = 1
i_col = m - 1
i_row = 0

isExistent = False
# Поиск нужной строки
while not isExistent:
    isExistent = matr[i_row][i_col] == k
    if isExistent:
        break
    count += 1
...