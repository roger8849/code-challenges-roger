
def string_to_int(s: str)-> int:
    # If the number represented as a string
    # contains only a single digit
    # then returns its value
    if (len(s) == 1):
        return ord(s[0]) - ord('0')
 
    # Recursive call for the sub-string
    # starting at the second character
    y = string_to_int(s[1:])
 
    # First digit of the number
    x = ord(s[0]) - ord('0')
 
    # First digit multiplied by the
    # appropriate power of 10 and then
    # add the recursive result
    # For example, xy = ((x * 10) + y)
    x = x * (10**(len(s) - 1)) + y
    return x

def main():
    s = input('Enter a number: ')
    print(f'converting {s} to a number - 1 = {string_to_int(s) - 1}')

if __name__ == "__main__":
    main()