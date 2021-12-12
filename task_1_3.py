number = int(input('Введите число процентов о 1 до 100: '))
if number == 11 or number == 12 or number == 13 or number == 14 or 4 < number % 10 <= 9 or number % 10 == 0:
    x = 'процентов'
elif 1 < number % 10 < 5:
    x = 'процента'
else:
    x = 'процент'
print(number, x)