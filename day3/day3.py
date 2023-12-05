import re


def parse_engine_schematic():
    with open("input.txt") as f:
        schematic = ["." + row.strip().replace("+", "$").replace("-", "$") + "." for row in f]
        schematic.insert(0, "." * len(schematic[0]))
        schematic.append("." * len(schematic[0]))

    return schematic


def is_symbol(char):
    return char != "." and not char.isalnum()


def get_left_right_parts(schematic, x, y):
    return [get_num(schematic[y][:x], -1), get_num(schematic[y][x + 1:], 0)]


def get_above_below_parts(schematic, x, y):
    parts = []
    for y in [y - 1, y + 1]:
        if schematic[y][x].isnumeric():
            start_index = x
            while start_index > 0:
                if not schematic[y][start_index].isnumeric():
                    break
                start_index -= 1
            end_index = x
            while end_index < len(schematic[y]):
                if not schematic[y][end_index].isnumeric():
                    break
                end_index += 1
            parts.append(int(schematic[y][start_index+1:end_index]))
        else:
            parts += get_left_right_parts(schematic, x, y)

    return parts



def get_part(schematic, x, y):
    num = get_num(schematic[y][x:], 0)

    if is_part(num, schematic, x, y):
        return num
    return 0


def is_part(num, schematic, x, y):
    num_len = len(str(num))
    # could probably just make the string and regex for symbol instead? :shrug:
    return (
        any(is_symbol(char) for char in schematic[y - 1][x - 1 : x + num_len + 1])
        or any(is_symbol(char) for char in schematic[y + 1][x - 1 : x + num_len + 1])
        or is_symbol(schematic[y][x - 1])
        or is_symbol(schematic[y][x + num_len])
    )


def get_num(schematic_slice, index):
    
    
    if not schematic_slice[index].isnumeric():
        return 0
    
    nums = re.findall(r"\d+", schematic_slice)
    if len(nums) > 0:
        return int(nums[index])
    return 0


def get_gear_ratio(schematic, x, y):
    parts = []
    a = get_left_right_parts(schematic, x, y)
    
    b = get_above_below_parts(schematic, x, y)
    
    parts += a
    parts += b
    
    parts = list(filter(lambda x: x > 0, parts))
    
    print(f"2Found gear at {x, y} with parts: {parts}")

    if len(parts) == 2:
        return parts[0] * parts[1]

    return 0


def __main__():
    schematic = parse_engine_schematic()
    from pprint import pprint

    parts_sum = 0
    gear_sum = 0
    gear_counter = 0

    y = 0
    while y < len(schematic):
        x = 0
        while x < len(schematic[y]):
            if schematic[y][x].isnumeric():  # part 1
                part_num = get_part(schematic, x, y)
                x = x + len(str(part_num)) - 1 # we always add 1 at end
                parts_sum += part_num
            elif schematic[y][x] == "*":  # part 2
                gear_counter += 1
                gear_sum += get_gear_ratio(schematic, x, y)

            x += 1

        y += 1

    print(f"Sum of parts: {parts_sum}")
    print(f"Sum of gear ratios: {gear_sum}")
    print(gear_counter)


__main__()
