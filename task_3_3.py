def thesaurus(*names):
    my_dict = {}
    for name in names:
        key = name[0].capitalize()
        if key not in my_dict:
            my_dict[key] = []
        my_dict[key].append(name)
    return my_dict


print(thesaurus("Иван", "Мария", "Петр", "Илья"))