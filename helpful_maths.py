def main():
    sum_on_the_board = input()
    sorted_numbers = sorted(sum_on_the_board.split(sep='+'))
    rewritten_sum = ''.join(number + '+' for number in sorted_numbers)[:-1]
    print(rewritten_sum)


if __name__ == '__main__':
    main()
