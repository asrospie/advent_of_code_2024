import re

def parse_input(filename):
    robots = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            nums = [ int(x) for x in re.findall('-?[0-9]+', line) ]
            robots.append([[nums[0], nums[1]], [nums[2], nums[3]]])
    return robots


def print_grid(robots, x_max, y_max, x_mid, y_mid):
    grid = [ [ 0 for _ in range(x_max) ] for _ in range(y_max) ]
    
    for r in robots:
        pos = r[0]
        grid[pos[1]][pos[0]] += 1


    for y in range(y_max):
        for x in range(x_max):
            if x == x_mid or y == y_mid:
                print('.', end='')
            else:
                print(grid[y][x], end='')
        print()


def print_grid_tree(robots, x_max, y_max):
    grid = [ [ 0 for _ in range(x_max) ] for _ in range(y_max) ]
    
    for r in robots:
        pos = r[0]
        grid[pos[1]][pos[0]] += 1


    for y in range(y_max):
        for x in range(x_max):
            if grid[y][x] == 0:
                print('.', end='')
            else: 
                print('#', end='')
        print()


def find_grid_tree(robots, x_max):
    grid = [ 0 for _ in range(x_max) ]

    for r in robots:
        if r[0][1] == 0:
            grid[r[0][1]] += 1


    return all([ x > 0 for x in grid ])


def move_robot(r, x_max, y_max):
    pos = r[0]
    v = r[1]

    pos[0] += v[0]
    pos[1] += v[1]

    if pos[0] >= x_max:
        pos[0] = pos[0] - x_max
    if pos[1] >= y_max:
        pos[1] = pos[1] - y_max
    if pos[0] < 0:
        pos[0] = x_max + pos[0]
    if pos[1] < 0:
        pos[1] = y_max + pos[1]

    return [pos, v]


def find_safety_factor(robots, x_max, y_max, x_mid, y_mid):
    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0
    for r in robots:
        pos = r[0]
        # q1
        if pos[0] >= 0 and pos[0] < x_mid and pos[1] >= 0 and pos[1] < y_mid:
            q1 += 1
        # q2
        elif pos[0] > x_mid and pos[0] < x_max and pos[1] >= 0 and pos[1] < y_mid:
            q2 += 1
        # q3
        elif pos[0] >= 0 and pos[0] < x_mid and pos[1] > y_mid and pos[1] < y_max:
            q3 += 1
        # q4
        elif pos[0] > x_mid and pos[0] < x_max and pos[1] > y_mid and pos[1] < y_max:
            q4 += 1

    return q1 * q2 * q3 * q4


def day_14_part_1(filename, x_max, y_max):
    robots = parse_input(filename)

    y_mid = int(y_max / 2)
    x_mid = int(x_max / 2)

    seconds_elapsed = 100


    for _ in range(seconds_elapsed):
        robots = list(map(lambda x: move_robot(x, x_max, y_max), robots))

    return find_safety_factor(robots, x_max, y_max, x_mid, y_mid)



# look for lowest safety factor
def day_14_part_2(filename, x_max, y_max, seconds_elapsed):
    robots = parse_input(filename)

    y_mid = int(y_max / 2)
    x_mid = int(x_max / 2)

    sfs = []
    for _ in range(seconds_elapsed):
        robots = list(map(lambda x: move_robot(x, x_max, y_max), robots))
        sfs.append(find_safety_factor(robots, x_max, y_max, x_mid, y_mid))

    return sfs.index(min(sfs)) + 1


def main():
    print(day_14_part_1('day_14.test', 11, 7))
    print(day_14_part_1('day_14.input', 101, 103))
    print(day_14_part_2('day_14.input', 101, 103, 10_000))

if __name__ == '__main__':
    main()
