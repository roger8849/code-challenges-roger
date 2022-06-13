from typing import List

def remove_consecutive_duplicates_recursively(s: str) -> str:
    if len(s) < 2:
        return s

    if s[0] == s[1]:
        return remove_consecutive_duplicates_recursively(s[1:])
    return s[0] + remove_consecutive_duplicates_recursively(s[1:])



def main():
    s = 'aaabbbccaadeefgg'
    s2 = remove_consecutive_duplicates_recursively(s)
    print(f'array {s} after removing consectuvie duplicates is {s2}')

if __name__ == "__main__":
    main()