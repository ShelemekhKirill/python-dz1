# Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно,
# что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?
# Пример:
# No 6 -> 1 4 1
# No 24 -> 4 16 4
# No 60 -> 10 40 10

zyr = input('Видите количество всех изготовлиных журавликов: ')
zyr = int(zyr)
print('Всего изготовлено журавликов', zyr)
KPS=(zyr//3)
Kat=(KPS*2)
Pet=(Kat//4)
Ser=(Kat//4)
print('Катя сделала:', Kat)
print('Петя сделал:', Pet)
print('Сережа сделал:', Ser)