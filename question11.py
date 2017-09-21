loop_variable = True
while loop_variable:
    print('e.g. password1, password2, password3,.....')
    passwords = input('Enter coma separated passwords:\n')
    passwords = passwords.split(', ')
    validate_password = [False, False, False, False, False]
    accepted_password = ''
    for password in passwords:
        for p in password:
            if ord(p) >=65 and ord(p) <= 90:
                validate_password[0] = True
            if ord(p) >=97 and ord(p) <= 122:
                validate_password[1] = True
            if p == '@' or p == '$' or p == '#':
                validate_password[2] = True
        if len(password) >= 6 and len(password) <= 12:
            validate_password[3] = True
        if validate_password[0] and validate_password[1] and validate_password[2] and validate_password[3]:
            validate_password[4] = True
            accepted_password = password
            break
    if validate_password[4]:
        print('Accepted password =', accepted_password)
        loop_variable = False

    else:
        my_input = input('Password not accepted! do want to try again? (y/n)')
        if my_input == 'y' or my_input == 'Y':
            continue
        else:
            loop_variable = False

