import re
import numpy as np


def parse_input(filename):
    lst = []
    with open(filename, 'r') as f:
        temp = []
        for line in f.readlines():
            if len(line) <= 1:
                continue
            nums = re.findall(r'[0-9]+', line)
            if nums:
                temp.append((int(nums[0]), int(nums[1])))
            if len(temp) == 3:
                lst.append(temp)
                temp = []
    return lst


def day_13_part_1(filename):
    lst = parse_input(filename)

    result = 0
    for l in lst:
        a = np.array([[l[0][0], l[1][0]], [l[0][1], l[1][1]]])
        b = np.array([l[2][0], l[2][1]])
        x = np.linalg.solve(a, b)
        x = np.round(x, 4)
        if int(x[0]) - x[0] == 0  and int(x[1]) - x[1] == 0:
            result += 3 * int(x[0]) + int(x[1])

    return result


def day_13_part_2(filename):
    lst = parse_input(filename)
    result = 0

    prize_modifier = 10_000_000_000_000
    for l in lst:
        a = np.array([[l[0][0], l[1][0]], [l[0][1], l[1][1]]])
        b = np.array([l[2][0] + prize_modifier, l[2][1] + prize_modifier])
        x = np.linalg.solve(a, b)
        x = np.round(x, 4)
        if int(x[0]) - x[0] == 0  and int(x[1]) - x[1] == 0:
            result += 3 * int(x[0]) + int(x[1])

    return result


def main():
    print(day_13_part_1('day_13.test'))
    print(day_13_part_1('day_13.input'))
    print(day_13_part_2('day_13.test'))
    print(day_13_part_2('day_13.input'))


if __name__ == '__main__':
    main()
