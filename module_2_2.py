first=int(input("Введите целое число: "))
second=int(input("Введите целое число: "))
third=int(input("Введите целое число: "))

if first == second == third:
    print('Вывод: 3')
elif first == second or first == third or second == third:
    print('Вывод: 2')
else:
    print('Вывод: 0')
