'''Задача 1. Сортировка трёх чисел'''

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

if a > b and b > c:
  print(c, b, a)
elif b > c and c > a:
  print(a, c, b)
elif b > a and a > c:
  print(c, a, b)
elif c > a and a > b:
  print(b, a, c)
elif a > b and c > b:
  print(b, c, a)
else:
  print(a, b, c)