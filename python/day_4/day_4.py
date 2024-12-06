def check_out_of_bounds(x, y, check, len_x, len_y):
    x_check = all([ x + v[0] < len_x and x + v[0] >= 0 for v in check ])
    y_check = all([ y + v[1] < len_y and y + v[1] >= 0 for v in check ])

    return x_check and y_check


def day_4_part_1(filename: str):
    with open(filename, 'r') as file:
        grid = [ x.strip() for x in file.readlines() ]

    checks = [
        [[1, 1], [2, 2], [3, 3]],
        [[-1, -1], [-2, -2], [-3, -3]],
        [[1, -1], [2, -2], [3, -3]],
        [[-1, 1], [-2, 2], [-3, 3]],
        [[1, 0], [2, 0], [3, 0]],
        [[-1, 0], [-2, 0], [-3, 0]],
        [[0, 1], [0, 2], [0, 3]],
        [[0, -1], [0, -2], [0, -3]]
    ]

    len_x = len(grid[0])
    len_y = len(grid)

    result = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 'X':
                for check in checks:
                    if not check_out_of_bounds(x, y, check, len_x, len_y):
                        continue
                    if grid[y + check[0][1]][x + check[0][0]] == 'M' and \
                        grid[y + check[1][1]][x + check[1][0]] == 'A' and \
                        grid[y + check[2][1]][x + check[2][0]] == 'S':
                        result += 1

    return result


def day_4_part_2(filename: str): 
    with open(filename, 'r') as file:
        grid = [ x.strip() for x in file.readlines() ]

    len_x = len(grid[0])
    len_y = len(grid)

    check = [[1, 1], [-1, -1], [1, -1], [-1, 1]]

    result = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 'A':
                if not check_out_of_bounds(x, y, check, len_x, len_y):
                    continue
                if ((grid[y + check[0][1]][x + check[0][0]] == 'M' and grid[y + check[1][1]][x + check[1][0]] == 'S') or \
                    (grid[y + check[0][1]][x + check[0][0]] == 'S' and grid[y + check[1][1]][x + check[1][0]] == 'M')) and \
                    ((grid[y + check[2][1]][x + check[2][0]] == 'M' and grid[y + check[3][1]][x + check[3][0]] == 'S') or \
                    (grid[y + check[2][1]][x + check[2][0]] == 'S' and grid[y + check[3][1]][x + check[3][0]] == 'M')):
                    result += 1

    return result



def main():
    print(day_4_part_1('test4.txt'))
    print(day_4_part_1('day4.input'))
    print(day_4_part_2('test4_2.txt'))
    print(day_4_part_2('day4.input'))


if __name__ == '__main__':
    main()
