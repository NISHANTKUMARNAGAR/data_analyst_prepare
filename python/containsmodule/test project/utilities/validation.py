def checkint(i):
    try:
        if  not str.isdigit(i):
            raise ValueError
    except ValueError:
        print("given value is not a integer")