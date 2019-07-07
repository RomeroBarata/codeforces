def main():
    n = int(input())
    for _ in range(n):
        word = input()
        if len(word) <= 10:
            print(word)
            continue
        first_char, last_char = word[0], word[-1]
        num_letters_in_between = len(word[1:-1])
        print(first_char, num_letters_in_between, last_char, sep='')


if __name__ == '__main__':
    main()
