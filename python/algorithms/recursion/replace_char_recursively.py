from typing import List

def replace_char_recursively(word, to_replace, replacement):
    # Base case
    if word == []:
        return word

    # Induction step.
    if word[0] == to_replace:
        word[0] = replacement
    # Need to be slice because cannot concatenate string with list
    word =  word[:1] + replace_char_recursively(word[1:], to_replace, replacement)
    return word
    

def main():
    word = list(input('Enter a word: '))
    find = input('Enter char to replace letter: ')
    replacement = input('Enter replacement letter: ')

    print(f'Replace replace letter {find} with {replacement} of word {"".join(word)} is:')
    word = replace_char_recursively(word, find, replacement)
    print(''.join(word))

    # print(replace([3,2,1,3,2,1], 1, 4))
    

if __name__ == "__main__":
    main()