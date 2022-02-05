my_list = [35.19, 524, 27.9, 56, 57.2, 94.63, 25.5, 2008.01, 3.27, 56.19, 46, 31.06, 108.56, 255.4, 7922.1]
my_list_new = []
for number in my_list:
    number *= 100
    rubles = int(number) // 100
    penny = int(number) % 100
    values = ''.join(f'{rubles:02d} руб. {penny:02d} коп.')
    my_list_new.append(values)
print(', '.join(my_list_new))

my_sort_list = my_list
my_sort_list.sort()
my_list_new = []
for number in my_sort_list:
    number *= 100
    rubles = int(number) // 100
    penny = int(number) % 100
    values = ''.join(f'{rubles:02d} руб. {penny:02d} коп.')
    my_list_new.append(values)
print(', '.join(my_list_new))
print(id(my_list))
print(id(my_sort_list))

my_descending_list = my_list
my_descending_list.sort()
my_descending_list.reverse()
my_list_new = []
for number in my_sort_list:
    number *= 100
    rubles = int(number) // 100
    penny = int(number) % 100
    values = ''.join(f'{rubles:02d} руб. {penny:02d} коп.')
    my_list_new.append(values)
print(', '.join(my_list_new))
print(id(my_list))
print(id(my_descending_list))

for top5 in my_descending_list[:5]:
    print(top5)
