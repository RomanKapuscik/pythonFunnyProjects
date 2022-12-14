
print('Dla f(x) = a * x ** 2 + b * x + c popdaj: \n')

a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))


def f(a: int, b: int, c: int):
    """Funkcja obliczająca miejsca zetowe równania kwadratowego postaci f(x) = a * x ** 2 + b * x + c

    :param a: int
    :param b: int
    :param c: int
    :return: miejsca zerowe jeśli istnieją
    """

    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b - delta ** 1/2)/(2 * a)
        x2 = (-b + delta ** 1/2)/(2 * a)
        print(f'x1= {x1}, x2= {x2}')
        return x1, x2
    elif delta == 0:
        x = -(b/2*a)
        print(f'x= {x}')
        return x
    print('Dla delta<0 brak miejsc zerowych')
    return None


f(a, b, c)

# f(-4, 2, -5)
# f(2, 4, 2)
# f(1, 6, 8)

