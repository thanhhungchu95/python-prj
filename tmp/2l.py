import math

def func(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                print('Infinite.')
            else:
                print('None.')
        else:
            print('x =', -c / b, '.')
    else:
        delta = b * b - 4 * a * c
        if delta < 0:
            print('x1 =', -b / (2 * a), '+', math.sqrt(-delta) / (2 * a), '* i')
            print('x2 =', -b / (2 * a), '-', math.sqrt(-delta) / (2 * a), '* i')
        else:
            if delta == 0:
                print('x =', -b / (2 * a), '.')
            else:
                print('x1 =', (-b + math.sqrt(delta)) / (2 * a))
                print('x2 =', (-b - math.sqrt(delta)) / (2 * a))

func(1, 2, 3)
