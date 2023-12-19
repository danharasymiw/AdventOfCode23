from itertools import pairwise


def solve_row(row):
    sum = 0

    while not all(num == 0 for num in row):
        sum += row[-1]
        row = [y - x for (x, y) in pairwise(row)]

    return sum


def __main__():
    f = open("input.txt")
    lines = f.readlines()
    input = []
    reversed_input = []
    for line in lines:
        nums = list(map(lambda x: int(x), line.split(" ")))
        input.append(nums)
        reversed_nums = list(reversed(nums))
        reversed_input.append(reversed_nums)

    sum = 0
    for row in input:
        sum = solve_row(row)
    print(f"Part 1: {sum}")

    # Is there a more efficient way of doing this? Yes
    # Does reversing the list and just using the same function solve it? Also Yes
    sum = 0
    for row in reversed_input:
        sum += solve_row(row)
    print(f"Part 2: {sum}")


__main__()
