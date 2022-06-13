
from inspect import _void


def print_subsequences(input_str: str, output_str: str, vector: str) -> _void:
    #  Base case.
    if not input_str:
        print(output_str)
        vector.append(output_str)
        return
    
    print_subsequences(input_str[1:], output_str + input_str[0], vector) # include first char
    print_subsequences(input_str[1:], output_str, vector) # exclude first char

def main():
    input_str = input('Insert string: ')
    vector = list()
    print_subsequences(input_str, str(), vector)
    
    print(vector)

if __name__ == "__main__":
    main()

