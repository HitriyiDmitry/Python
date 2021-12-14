# 5A
my_list = [35.19, 27.9, 56, 57.2, 94.63, 25.5, 3.27, 56.19, 46, 31.06, 108.56, 255.4, 524, 2008.01, 7922.1]
my_list_new = []
for number in my_list:
    number *= 100
    rubles = int(number) // 100
    penny = int(number) % 100
    values = ''.join(f'{rubles:02d} руб. {penny:02d} коп.')
    my_list_new.append(values)
print(', '.join(my_list_new))

# 5B
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

# 5C
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

# 5D
print(my_descending_list[:5])

# Следующим по длине будет код через цикл for, корый будет записывать каждое значение исходного списка и сравнивать его с
# последующим, записывая максимальное значение в новый список и удаляя его из исходного списка
# (одина из первых задач на цикл for)