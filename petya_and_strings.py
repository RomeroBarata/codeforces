def main():
    first_string = input().lower()
    second_string = input().lower()
    if first_string < second_string:
        print(-1)
    elif first_string > second_string:
        print(1)
    else:
        print(0)


if __name__ == '__main__':
    main()
