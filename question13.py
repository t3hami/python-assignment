class Generator():
    def __init__(self,number):
        self.number = number

    def generator_function(self):
        for n in range(7, self.number+1, 7):
            yield n

input_number = -1
while not input_number > 0:
    input_number = int(input('Enter range: '))
    if not input_number > 0:
        print('Please enter a positive number')
g = Generator(input_number)
for i in g.generator_function():
    print(str(i))
