my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

new_list = []
for number in my_list:
    if number.isdigit():
        new_list.extend(['"', f'{int(number):02}', '"'])
    elif (number.startswith('+') or number.startswith('-')) and number[1:].isdigit():
        new_list.extend(['"', f'{number[0]}{int(number[1:]):02}', '"'])
    else:
        new_list.append(number)

print(' '.join(new_list))
