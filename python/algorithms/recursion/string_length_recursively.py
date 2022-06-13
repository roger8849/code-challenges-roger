def length_recursively(word: str) -> int:
    # Base case
    if not word:
        return 0
    # Induction hipotesis
    small_answer = length_recursively(word[1:])
    # Induction step.
    return 1 + small_answer
    


def main():
    word = input('Enter a word: ')

    print(f'Length of the word {word} is {length_recursively(word)}')
    

if __name__ == "__main__":
    main()