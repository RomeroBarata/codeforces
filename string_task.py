VOWELS = 'aeiouy'
VOWELS_TO_NULL = dict.fromkeys(VOWELS)
TRANSLATION_TABLE = str.maketrans(VOWELS_TO_NULL)


def main():
    word = input().lower()
    word = word.translate(TRANSLATION_TABLE)
    if word:
        for ch in word:
            print('.', ch, sep='', end='')
    print()


if __name__ == '__main__':
    main()
