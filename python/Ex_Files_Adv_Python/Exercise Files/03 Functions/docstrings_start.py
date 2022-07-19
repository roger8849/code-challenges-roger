# Demonstrate the use of function docstrings


def myFunction(arg1, arg2=None):
    """function doing something

    Args:
        arg1 (_type_): _description_
        arg2 (_type_, optional): _description_. Defaults to None.
    """
    print(arg1, arg2)


def main():
    print(myFunction.__doc__)


if __name__ == "__main__":
    main()
