import math


def main():
    problem_values = input()
    n, m, a = [int(value) for value in problem_values.split()]
    flagstones = math.ceil(n / a) * math.ceil(m / a)
    print(flagstones)


if __name__ == '__main__':
    main()
