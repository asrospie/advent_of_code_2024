from collections import deque, defaultdict


def find_adjacent(grid, curr):
    adj = []
    cx, cy = curr[0], curr[1]
    val = grid[cy][cx]

    if cx - 1 >= 0 and grid[cy][cx - 1] == val:
        adj.append((cx - 1, cy))
    if cx + 1 < len(grid[0]) and grid[cy][cx + 1] == val:
        adj.append((cx + 1, cy))
    if cy - 1 >= 0 and grid[cy - 1][cx] == val:
        adj.append((cx, cy - 1))
    if cy + 1 < len(grid) and grid[cy + 1][cx] == val:
        adj.append((cx, cy + 1))
    return adj


def solve(filename, method):
    with open(filename, 'r') as f:
        grid = [ [ c for c in row.strip() ] for row in f.readlines() ]

    result = 0
    plotted = defaultdict(list)
    for y, r in enumerate(grid):
        for x, c in enumerate(r):
            if (x, y) in plotted[c]:
                continue
            plotted[c].append((x, y))

            # bfs to find plots of (x, y)
            visited = [(x, y)]
            q = deque()
            q.append((x, y))
            while q:
                curr = q.popleft()
                for v in find_adjacent(grid, curr):
                    if v not in visited:
                        plotted[c].append(v)
                        visited.append(v)
                        q.append(v)
            
            result += method(visited, grid, c)

    return result

def day_12_part_1(filename):
    def method(visited, grid, c):
        perimiter = 0
        for v in visited:
            vx, vy = v[0], v[1]
            if vx - 1 < 0 or grid[vy][vx - 1] != c:
                perimiter += 1
            if vx + 1 >= len(grid[0]) or grid[vy][vx + 1] != c:
                perimiter += 1
            if vy - 1 < 0 or grid[vy - 1][vx] != c:
                perimiter += 1
            if vy + 1 >= len(grid) or grid[vy + 1][vx] != c:
                perimiter += 1

        return len(visited) * perimiter

    return solve(filename, method)


def day_12_part_2(filename):

    def method(visited, grid, c):
        side_count = 0
        sides = { 'left': [], 'right': [], 'up': [], 'down': [] }
        for v in visited:
            vx, vy = v[0], v[1]
            if vx - 1 < 0 or grid[vy][vx - 1] != c:
                sides['left'].append(v)
            if vx + 1 >= len(grid[0]) or grid[vy][vx + 1] != c:
                sides['right'].append(v)
            if vy - 1 < 0 or grid[vy - 1][vx] != c:
                sides['up'].append(v)
            if vy + 1 >= len(grid) or grid[vy + 1][vx] != c:
                sides['down'].append(v)

        for k, v in sides.items():
            t = []
            if k == 'left' or k == 'right':
                t = sorted(v, key=lambda x: x[1])
                t = list(filter(lambda v: (v[0], v[1] + 1) not in t, t))
            else:
                t = sorted(v, key=lambda x: x[0])
                t = list(filter(lambda v: (v[0] + 1, v[1]) not in t, t))
            side_count += len(t)

        return len(visited) * side_count

    return solve(filename, method)


def main():
    print(day_12_part_1('day_12.test'))
    print(day_12_part_1('day_12.input'))
    print(day_12_part_2('day_12.test'))
    print(day_12_part_2('day_12.input'))


if __name__ == '__main__':
    main()
