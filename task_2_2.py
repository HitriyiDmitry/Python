my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_list = []
for elem in my_list:
    if elem.isdigit():
        new_list.extend(['"', f'{int(elem):02}', '"'])
    elif (elem.startswith('+') or elem.startswith('-')) and elem[1:].isdigit():
        new_list.extend(['"', f'{elem[0]}{int(elem[1:]):02}', '"'])
    else:
        new_list.append(elem)
out_info = ' '.join(new_list)
print(out_info)

delete_space_list = []
for idx, letter in enumerate(out_info):
    if letter == '"':
        delete_space_list.append(idx)
for idx in range(len(delete_space_list)):
    if idx % 2 == 0:
        delete_space_list[idx] = delete_space_list[idx] + 1
    else:
        delete_space_list[idx] = delete_space_list[idx] - 1
for del_idx in reversed(delete_space_list):
    out_info = out_info[:del_idx] + out_info[del_idx + 1:]
print(out_info)
