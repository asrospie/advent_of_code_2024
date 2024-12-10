from collections import defaultdict, deque


def display_grid(grid):
    for r in grid:
        for c in r:
            print(c, end='')
        print()


def find_trailheads(grid):
    ts = []
    for y, r in enumerate(grid):
        for x, c in enumerate(r):
            if c == 0:
                ts.append((x, y))
    return ts


def find_adjacent(grid, curr):
    adj = []
    cx, cy = curr[0], curr[1]
    val = grid[cy][cx]
    if cx - 1 >= 0 and grid[cy][cx - 1] - val == 1:
        adj.append((cx - 1, cy))
    if cx + 1 < len(grid[0]) and grid[cy][cx + 1] - val == 1:
        adj.append((cx + 1, cy))
    if cy - 1 >= 0 and grid[cy - 1][cx] - val == 1:
        adj.append((cx, cy - 1))
    if cy + 1 < len(grid) and grid[cy + 1][cx] - val == 1:
        adj.append((cx, cy + 1))
    return adj


def day_10_part_1(filename):
    grid = []
    with open(filename, 'r') as f:
        grid = [ [ int(c) for c in line.strip() ] for line in f.readlines() ]

    trailheads = find_trailheads(grid)

    result = 0
    for head in trailheads:
        q = deque()
        visited = set()
        q.append(head)
        while q:
            curr = q.popleft()

            for x in find_adjacent(grid, curr):
                if x not in visited:
                    visited.add(x)
                    q.append(x)
        result += len(list(filter(lambda v: grid[v[1]][v[0]] == 9, list(visited))))

    return result


def day_10_part_2(filename):
    grid = []
    with open(filename, 'r') as f:
        grid = [ [ int(c) for c in line.strip() ] for line in f.readlines() ]

    trailheads = find_trailheads(grid)

    result = 0
    for head in trailheads:
        q = deque()
        visited = set()
        q.append(head)
        path_count = defaultdict(int)
        path_count[head] = 1
        while q:
            curr = q.popleft()

            for x in find_adjacent(grid, curr):
                path_count[x] += path_count[curr]
                if x not in visited:
                    visited.add(x)
                    q.append(x)
        nines = list(filter(lambda x: grid[x[1]][x[0]] == 9, list(visited)))
        for n in nines:
            result += path_count[n]

    return result


def main():
    print(day_10_part_1('day_10.test'))
    print(day_10_part_1('day_10.input'))
    print(day_10_part_2('day_10.test'))
    print(day_10_part_2('day_10.input'))


if __name__ == '__main__':
    main()
