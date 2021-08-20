def fun(a, b):
    if a > b:
        print(a)
    else:
        print(b)


def get_arg(arg_name):
    while not (arg := input(f'Input number {arg_name}: ')).isnumeric():
        pass
    return arg


x = get_arg('x')
y = get_arg('y')
fun(x, y)
