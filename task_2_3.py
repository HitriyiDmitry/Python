my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
number = 0
while number < len(my_list):
    if my_list[number].isdigit():
        my_list.insert(number, '"')
        my_list[number + 1] = f'{int(my_list[number +1]):02}'
        my_list.insert(number + 2, '"')
        number += 3
    elif (my_list[number].startswith('+') or my_list[number].startswith('-')) and my_list[number][1:].isdigit():
        my_list.insert(number, '"')
        my_list[number + 1] = f'{my_list[number + 1][0]}{int(my_list[number + 1]):02}'
        my_list.insert(number + 2, '"')
        number += 3
    number += 1
print(' '.join(my_list))