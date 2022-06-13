
from inspect import _void


def print_str(s: str, reversed=False) -> _void:
    if not s:
        return

    if reversed:
        print_str(s[1:], reversed)
        print(s[0], end=' ')
    else: 
        print(s[0], end=' ')
        print_str(s[1:])

def main():
    word = input('Enter a word to print: ')
    print_str(word)
    print()
    print_str(word, True)
    print()


if __name__ == "__main__":
    main()