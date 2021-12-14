my_list = ['инженер-кончтруктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАЙ', 'директор аэлита']
for element in my_list:
    *position, name = element.split()
    name = name.title()
    print(f'Привет {name}!')
