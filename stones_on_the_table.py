def main():
    _ = int(input())
    colours = input()
    min_stones_to_remove = 0
    previous_colour = colours[0]
    for colour in colours[1:]:
        if colour == previous_colour:
            min_stones_to_remove += 1
        previous_colour = colour
    print(min_stones_to_remove)


if __name__ == '__main__':
    main()
