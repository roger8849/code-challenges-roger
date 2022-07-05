

from concurrent.futures import ThreadPoolExecutor


def are_reversed(word1, word2):
    if not word1 and not word2:
        return True
    if len(word1) != len(word2):
        return False
    for i, j in zip(range(len(word1)), range(len(word2) - 1, -1, -1)):
        if word1[i] != word2[j]:
            return False
    return True

def main():

    assert are_reversed('ACD', 'DCA')
    assert not are_reversed('ACDAAA', 'DCADSW')
    assert not are_reversed('ACD', '')


if __name__ == "__main__":
    main()
