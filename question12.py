
list_of_tuples = []


def fill_list():
    name = input('Enter name\t:\t')
    age = int(input('Enter age\t:\t'))
    height = int(input('Enter height\t:\t'))
    list_of_tuples.append((name, age, height))
    print('Information added!')

take_input = 'y'
while take_input == 'y' or take_input == 'Y':
    fill_list()
    i = input('Do you want to put more information? (y/n)')
    if i == take_input or i == 'Y':
        continue
    else:
        break
sorted_list = sorted(list_of_tuples, key=lambda my_tuple: (my_tuple[0], my_tuple[1], my_tuple[2]))
print(sorted_list)