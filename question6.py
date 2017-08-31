def divide(n, d):
    try:
        return n/d
    except ZeroDivisionError:
        return 'Cannot divide by zero!'

numerator = int(input('Enter number: '))
denominator = int(input('Enter number: '))
print(str(divide(numerator, denominator)))
