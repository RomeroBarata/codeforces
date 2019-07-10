def is_even(n: int) -> bool:
    return (n % 2) == 0


def main():
    username = input()
    num_distinct_chars = len(set(username))
    if is_even(num_distinct_chars):
        print('CHAT WITH HER!')
    else:
        print('IGNORE HIM!')


if __name__ == '__main__':
    main()
