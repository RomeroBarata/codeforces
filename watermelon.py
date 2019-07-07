def is_even(n: int) -> bool:
    return (n % 2) == 0


def main():
    w = int(input())
    if is_even(w) and w != 2:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
