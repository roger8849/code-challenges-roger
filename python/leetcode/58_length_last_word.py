'''
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
 

Constraints:

1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.
'''
# Most efficient. Start at end and then count the chars
def lengthOfLastWord(s: str) -> int:
    length_last_word = 0
    i = len(s) - 1
    while i >= 0:
        letter = s[i]
        if letter != ' ':
            length_last_word +=1
        elif letter == ' ' and length_last_word > 0 :
            return length_last_word
        i -= 1
    return length_last_word


# Reverse approach: reverse the string and count the chars.
def lenghtOfLastWordReversed(s: str) -> int:
    length_last_word = 0
    s = s[::-1]
    i=0
    while(i < len(s)):
        letter = s[i]
        if letter != ' ':
            length_last_word +=1
        elif letter == ' ' and length_last_word > 0 :
            return length_last_word
        i += 1
    return length_last_word


# Naive approach start from the beggining and check all the letters.
def lengthOfLastWordNaive(s: str) -> int:
    length_last_word = 0

    iterator = iter(s)
    for letter in iterator:
        if letter != ' ':
            length_last_word += 1
        else:
            while letter == ' ':
                # Avoid problem when there is no next and the iterator is over.
                letter = next(iterator, None)
            else: 
                if letter == None:
                    return length_last_word
                else:
                    length_last_word=1
    return length_last_word

def main():
    phrase = input('Enter a word please: ')
    print(lengthOfLastWordNaive(phrase))
    print(lenghtOfLastWordReversed(phrase))

if __name__ == "__main__":
    main()