name = 'Наталья'
age = 18
print('Всем привет, меня зовут', name, 'и мне', age, 'лет')
a = (name + ' ') * 5
print(a)

b = input('Как вас зовут?')
c = input('Сколько вам лет?')
try:
    f = int(c)
    print('Ваш возраст', f)
except ValueError:
    print('Вы ввели число неверно. Попробуйте еще раз')
else:
    c = f

print('Привет', b)
if c <= 12:
    print('У тебя ещё не все молочные зубы выпали')
if 12 < c <= 18:
    print('А ты уже подготовился(лась) к экзаменам?')
if 18 < c <= 30:
    print('У тебя уже, наверное, есть седые волосы')
if 30 < c <= 60:
    print('С тебя уже песок сыпется')
if c > 60:
    print('Ты, наверное, такой мудрый')
print(name[2::])
print(name[::-1])
print(name[-3::])
print(name[:5:])
print(len(b))

if c < 100:
    s = 0
    d = c // 10
    r = c % 10
    s = d + r
    print(s)
    d = c // 10
    r = c % 10
    pr = d * r
    print(pr)

print(b.upper())
print(b.lower())
print(b.capitalize())
print(b.swapcase())

x = int(input('Сколько будет: 2+2*2?'))
if x == 6:
    print('Молодец! Ты правильно решил пример')
else:
    print('Подумай лучше!')

