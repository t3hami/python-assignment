input_string = input('Enter any string : ')
dict = {}
for i in sorted(set(input_string)):
    dict[i] = input_string.count(i)
for key, value in dict.items():
    print(key+', '+str(value))