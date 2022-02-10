def thesaurus_adv(*names_surnames):
    my_dict = {}
    for name_surname in names_surnames:
        name, surname = name_surname.split()
        my_dict.setdefault(surname[0], {})
        my_dict[surname[0]].setdefault(name[0], [])
        my_dict[surname[0]][name[0]].append(name_surname)

    my_dict_sort = {name: my_dict[name]
                    for name in sorted(my_dict)}
    return my_dict


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))