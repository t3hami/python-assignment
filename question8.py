from re import findall

my_string = input('Enter any string: ')
my_string = findall(r'\d{1,3}', my_string)
print(my_string)
