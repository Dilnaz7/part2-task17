print('''
Выберите филиал Google:
1) Казахстан
2) Париж
3) ЮАР
4) Кыргызстан
5) Сан-Франциско
6) Германия
7) Москва
8) Швеция''')

choise = int(input('Выберите номер филиала: '))

if choise == 1:
    kazakstan = open('google_offices/google_kazakhstan.txt', 'r+')