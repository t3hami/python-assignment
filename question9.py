def compute(n):
    answer = 0
    for i in range(1, n + 1):
        answer = answer + i / (i + 1)
    return answer

number = int(input('Enter any number: '))
print(str(compute(number)))