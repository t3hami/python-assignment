def f(n):
    if n > 0:
        return f(n-1)+100
    elif n == 0:
        return 0

print(str(f(2)))
