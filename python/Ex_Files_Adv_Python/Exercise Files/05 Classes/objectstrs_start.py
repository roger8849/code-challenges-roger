# customize string representations of objects


class Person():
    def __init__(self):
        self.fname = "Roger"
        self.lname = "Ramirez"
        self.age = 33

    # TODO: use __repr__ to create a string useful for debugging
    def __repr__(self) -> str:
        return '<Person Class - fname {0}, lname {1}, age {2}>'.format(self.fname, self.lname, self.age)

    # TODO: use str for a more human-readable string
    def __str__(self) -> str:
        return 'Person - fname {0}, lname {1}, age {2} '.format(self.fname, self.lname, self.age)

    def __bytes__(self):
        val = "Person:{0}:{1}:{2}".format(self.fname, self.lname, self.age)
        return bytes(val.encode('utf-8'))

def main():
    # create a new Person object
    cls1 = Person()

    # use different Python functions to convert it to a string
    print(repr(cls1))
    print(str(cls1))
    print("Formatted: {0}".format(cls1))
    print(f'bytes; {0}', cls1.__bytes__)


if __name__ == "__main__":
    main()
