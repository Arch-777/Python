def zero(a, b):
    try:
        c = a/b
    except ZeroDivisionError:
        print("Divide By Zero Error!!!")
    else:
        print("Result - ",c)
    finally:
        print("")


zero(10, 0)
zero(10, 2)
