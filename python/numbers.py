"""counting"""


def my_func():
    """a Func"""
    success = False
    while not success:
        try:
            anf = int(input("your starting number:"))
            success = True
        except ValueError:
            print("please use numbers")
    success = False
    while not success:
        try:
            ent = int(input("your ending number:"))
            success = True
        except ValueError:
            print("please use numbers")
    success = False
    while not success:
        try:
            steps = int(input("in what steps."))
            success = True
        except ValueError:
            print("please use numbers")

    for i in range(anf, ent, steps):
        print(i)


my_func()
