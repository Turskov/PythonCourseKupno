def test_print(a, b):
    if (a > b):
        print(a)
    else:
        print(b)

def test_return(a, b):
    if (a >= b):
        return a
    else:
        return b


a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
test_print(a, b)
c = test_return(a, b)
print(c)