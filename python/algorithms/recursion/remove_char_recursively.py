from typing import List


def remove_char_recursively_easy(word, to_replace):
    '''
        This approach do not remove the position just replace it with empty string and then join remove the char
    '''
    # Base case
    if word == []:
        return word

    # Induction step.
    if word[0] == to_replace:
        word[0] = ''
    # Need to be slice because cannot concatenate string with list
    word =  word[:1] + remove_char_recursively_easy(word[1:], to_replace)
    return word
    
def remove_char_recursively(word, to_remove):
    '''
        This aproach slice the list and remove the position, more corner cases to review.
    '''
    # Base case
    if word == []:
        return word

    # Induction step.
    if not word[0] == to_remove:
        remove_char_recursively(word[1:], to_remove)
    else:
        # Remove first element.
        word.pop(0)
        remove_char_recursively(word, to_remove)

# def replace(thelist,a,b):
#     #base case 1: thelist is empty
#     if thelist==[]:
#         return thelist
#     #case 1: the first character is a
#     elif thelist[0] == a:
#         thelist[0] = b
#     return thelist[:1] + replace(thelist[1:], a, b)




def main():
    word = list(input('Enter a word: '))
    find = input('Enter char to replace letter: ')

    print(f'Remove char {find} in  with word {"".join(word)} is:')
    word = remove_char_recursively(word, find)
    print(''.join(word))

    # print(replace([3,2,1,3,2,1], 1, 4))
    

if __name__ == "__main__":
    main()