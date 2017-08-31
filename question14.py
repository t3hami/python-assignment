import re
from math import sqrt
robot_position = (0, 0)
print('Note command: up, down, left, right e.g. --> up 20')
while True:
    my_string = input('tehami@robot:~/$ ')
    # use [command] [distance] to move robot
    command = re.search(r'[a-z]{1,5}', my_string, re.I | re.M)
    number = re.search(r'[0-9]{1,5}', my_string, re.I | re.M)
    if command.group() == 'up':
        robot_position = (robot_position[0], robot_position[1] + int(number.group()))
    elif command.group() == 'down':
        robot_position = (robot_position[0], robot_position[1] - int(number.group()))
    elif command.group() == 'left':
        robot_position = (robot_position[0] - int(number.group()), robot_position[1])
    elif command.group() == 'right':
        robot_position = (robot_position[0] + int(number.group()), robot_position[1])
    print('Current position of robot:', robot_position)
    input_ = input('Do you want to continue? (y/n) ')
    if input_ == 'y' or input_ == 'Y':
        continue
    else:
        break
distance = abs(sqrt(robot_position[0] * robot_position[0] + robot_position[1] * robot_position[1]))
print('Your robot covered ' + str(distance) + ' units from starting point!')
