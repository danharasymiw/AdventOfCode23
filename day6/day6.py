# there is probably a clever math solution to this
def solve(time, goal):
    num_solutions = 0
    goal_reached = False
    for t in range(1, time):
        speed = t
        time_remaining = time - t
        distance = speed * time_remaining

        if distance > goal:
            goal_reached = True
            num_solutions += 1
        elif goal_reached:  # exit when we found all solutions
            return num_solutions

    return num_solutions


def __main__():
    f = open("input.txt")
    lines = f.readlines()

    times = map(
        lambda s: int(s.strip()),
        filter(lambda s: len(s) != 0, lines[0].split(":")[1].split(" ")),
    )
    distances = map(
        lambda s: int(s.strip()),
        filter(lambda s: len(s) != 0, lines[1].split(":")[1].split(" ")),
    )

    answer = 1
    for time, distance in zip(times, distances):
        num = solve(time, distance)
        answer *= num

    print(answer)


__main__()
