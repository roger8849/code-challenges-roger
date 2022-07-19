# use iterator functions like enumerate, zip, iter, next


import os


def main():
    # define a list of days in English and French
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    daysFr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"]

    # TODO: use iter to create an iterator over a collection
    i = iter(days)
    print(next(i))
    print(next(i))
    print(next(i))

    # TODO: iterate using a function and a sentinel
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

    with open(os.path.join(__location__, 'testfile.txt'), 'r') as fp:
        for line in iter(fp.readline, ''):
            print(line)

    # TODO: use regular interation over the days
    for m in days:
        print(m)
    for m in range(len(days)):
        print(m+1, days[m])
    # TODO: using enumerate reduces code and provides a counter
    print('enumerate#######')
    for i,m in enumerate(days, start=1):
        print(i,m)
    # TODO: use zip to combine sequences
    for m in zip(days, daysFr):
        print(m)
    
    for i, m in enumerate(zip(days, daysFr)):
        print(i, m[0], ' = ', m[1], ' in french')


if __name__ == "__main__":
    main()
