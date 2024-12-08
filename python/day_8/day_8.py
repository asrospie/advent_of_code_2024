def display_grid(grid):
    for r in grid:
        for c in r:
            print(c[0], end='')
        print()


def x_y_diff(v0, v1):
    return v1[0] - v0[0], v1[1] - v0[1]


def day_8_part_1(filename):
    ants = {}
    with open(filename, 'r') as f:
        lines = f.readlines()
        x_len, y_len = len(lines[0]) - 1, len(lines)
        for y, r in enumerate(lines):
            for x, c in enumerate(r):
                if c == '.':
                    continue
                if c not in ants:
                    ants[c] = []
                ants[c].append((x, y))


    antinodes = set()
    for v in ants.values():
        for i, v0 in enumerate(v[:-1]):
            for v1 in v[i + 1:]:
                x_diff, y_diff = x_y_diff(v0, v1)
                dv0 = (v0[0] - x_diff, v0[1] - y_diff)
                dv1 = (v1[0] + x_diff, v1[1] + y_diff)

                if dv0[0] >= 0 and dv0[0] < x_len and dv0[1] >= 0 and dv0[1] < y_len:
                    antinodes.add(dv0)

                if dv1[0] >= 0 and dv1[0] < x_len and dv1[1] >= 0 and dv1[1] < y_len:
                    antinodes.add(dv1)


    return len(antinodes) 


def day_8_part_2(filename):
    ants = {}
    with open(filename, 'r') as f:
        lines = f.readlines()
        x_len, y_len = len(lines[0]) - 1, len(lines)
        for y, r in enumerate(lines):
            for x, c in enumerate(r):
                if c == '.':
                    continue
                if c not in ants:
                    ants[c] = []
                ants[c].append((x, y))


    antinodes = set()
    for v in ants.values():
        for i, v0 in enumerate(v[:-1]):
            for v1 in v[i + 1:]:
                x_diff, y_diff = x_y_diff(v0, v1)

                dv0 = v0
                dv1 = v1

                # go up
                while True:
                    if dv0[0] >= 0 and dv0[0] < x_len and dv0[1] >= 0 and dv0[1] < y_len:
                        antinodes.add(dv0)
                        dv0 = (dv0[0] - x_diff, dv0[1] - y_diff)
                        continue
                    break

                # go down
                while True:
                    if dv1[0] >= 0 and dv1[0] < x_len and dv1[1] >= 0 and dv1[1] < y_len:
                        antinodes.add(dv1)
                        dv1 = (dv1[0] + x_diff, dv1[1] + y_diff)
                        continue
                    break


    return len(antinodes) 


def main():
    print(day_8_part_1('day_8.test'))
    print(day_8_part_1('day_8.input'))
    print(day_8_part_2('day_8.test'))
    print(day_8_part_2('day_8.input'))

if __name__ == '__main__':
    main()
