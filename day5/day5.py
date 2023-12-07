import itertools


def calc_ranges(ranges, seed_map):
    next_ranges = []
    ranges = list(ranges)
    counter = 0
    for rang in ranges:
        found = False
        for row in seed_map:
            map_range = range(row[1], row[1] + row[2])
            range_start = max(rang.start, map_range.start)
            range_stop = min(rang.stop, map_range.stop)
            if range_start <= range_stop:
                found = True
                # map the range to the destination range
                start_index = range_start - map_range.start
                stop_index = range_stop - map_range.start
                new_range = range(row[0] + start_index, row[0] + stop_index)
                next_ranges.append(new_range)
                if rang.start < range_start:
                    new_range = range(rang.start, range_start - 1)
                    ranges.append(new_range)

                elif rang.stop > range_stop:
                    new_range = range(range_stop + 1, rang.stop)
                    ranges.append(new_range)

        if not found:
            next_ranges.append(rang)

    return next_ranges


def get_min_range_start(ranges):
    min_num = float("inf")
    for rang in ranges:
        if rang.start < min_num:
            min_num = rang.start
    return min_num


def list_to_ranges(nums):
    for a, b in itertools.groupby(enumerate(nums), lambda pair: pair[1] - pair[0]):
        b = list(b)
        yield range(b[0][1], b[-1][1])


def __main__():
    f = open("input.txt")
    lines = f.readlines()

    seeds = list(map(lambda x: int(x), lines[0][len("seeds: ") :].split(" ")))

    list_of_maps = []
    current_map = []
    for line in lines[3:]:
        if len(line) == 0 or line.isspace():
            continue
        elif ":" in line:  # start new map
            list_of_maps.append(current_map)
            current_map = []
        else:
            map_entry = list(map(lambda x: int(x), line.split(" ")))
            current_map.append(map_entry)
    list_of_maps.append(current_map)  # don't forget the last one

    # part 1
    ranges = list_to_ranges(seeds)

    for m in list_of_maps:
        ranges = calc_ranges(ranges, m)

    print(f"Part 1 min location: {get_min_range_start(ranges)}")

   # part 2
    ranges = []
    for i in range(0, len(seeds), 2):
        ranges.append(range(seeds[i], seeds[i] + seeds[i + 1]))

    for m in list_of_maps:
        ranges = calc_ranges(ranges, m)
    print(f"Part 2 min location: {get_min_range_start(ranges)}")


__main__()
