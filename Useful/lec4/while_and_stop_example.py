def fun(a, b):
    if a > b:
        print(a)
    else:
        print(b)


def get_arg(arg_name):

    while not (arg := input(f'Input number {arg_name}: ')).isnumeric():
        if arg == "stop":
            break
        elif arg == "!":
            continue
        print("Incorrect input")

    return arg


x = get_arg('x')
y = None
if x != "stop":
    y = get_arg('y')
    if y != "stop":
        fun(x, y)

if x == "stop" or y == "stop":
    print("OK")
