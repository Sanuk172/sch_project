a = input()
if a == '13':
    print('Брррр, холодрыга какая!')
elif a == '42':
    print('Ура, сегодня мой день ведь, я выйграл дом и 3 коровы.')
else:
    print('Ну булка хлеба, так булка хлеба.')



s = input()
while s != 'стоп':
    if 'Мана' or "мана" in s:
        print("абра кадабра")
    else:
        print("НЕТ")
    s = input()


for i in range(3):
    print(input() + ' Кррр!')



a = int(input())
b = int(input())
print(a + b)
c = a + b
if c / 3 == int(c / 3):
    print('Сумма стала волшебной')