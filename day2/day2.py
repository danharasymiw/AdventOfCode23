from functools import reduce

cubes_dict = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def is_valid_selection(cubes):
    for colour, num in cubes.items():
        if cubes_dict[colour] < num:
            return False

    return True


def __main__():
    game_counter = 0
    game_sum = 0  # part 1
    power = 0  # part 2

    with open("input.txt") as f:
        for game in f:
            game_counter += 1

            game = game[len(f"Game ${game_counter}:") :]
            hands_pulled = list(map(lambda x: x.strip(), game.split(";")))

            valid_hand = True
            min_cubes_dict = {}
            for hand_pulled in hands_pulled:
                hand_pulled_dict = {}

                for single_colour in hand_pulled.split(","):
                    num_str, colour = single_colour.strip().split(" ")
                    num = int(num_str)
                    hand_pulled_dict[colour] = num

                    if num > min_cubes_dict.get(colour, 0):
                        min_cubes_dict[colour] = num

                if not is_valid_selection(hand_pulled_dict):
                    valid_hand = False

            if valid_hand:
                game_sum += game_counter
            power += reduce(lambda x, y: x * y, min_cubes_dict.values())

    print(f"Sum of valid games: {game_sum}")
    print(f"Power level of games: {power}")


__main__()
