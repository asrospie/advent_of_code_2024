def find_last(lst):
    for i, v in enumerate(lst[::-1]):
        if v != '.':
            return len(lst) - 1 - i
    return -1


def print_grid(lst):
    for v in lst:
        if v[0] == -1:
            print('.' * v[1], end='')
        else:
            print(f'{str(v[0]) * v[1]}', end='')

    print()


def parse_input(filename):
    with open(filename, 'r') as f:
        s = f.readline().strip()

    is_file = True
    ls = []
    count = 0
    for c in s:
        if is_file:
            ls.extend([count] * int(c))
            count += 1
        else:
            ls.extend(['.'] * int(c))
        is_file = not is_file

    return ls


def day_9_part_1(filename):
    ls = parse_input(filename)
    for i, c in enumerate(ls):
        if c != '.':
            continue
        if len(set(ls[i:])) == 1:
            break
        last_idx = find_last(ls)
        ls[i], ls[last_idx] = ls[last_idx], ls[i]

    result = 0
    for i, v in enumerate(ls):
        if v == '.':
            continue
        result += i * int(v)

    return result


def day_9_part_2(filename):
    ls = []
    with open(filename, 'r') as f:
        count = 0
        is_file = True
        for c in f.readline().strip():
            if is_file:
                ls.append([count, int(c)])
                count += 1
            else:
                ls.append([-1, int(c)])
            is_file = not is_file


    i = len(ls) - 1
    while i >= 0:
        # skip blanks
        if ls[i][0] == -1:
            i -= 1
            continue

        # find swappable space
        swap_idx = -1
        for j, v in enumerate(ls):
            if j >= i:
                break
            if v[0] == -1 and v[1] >= ls[i][1]:
                swap_idx = j
                break
        if swap_idx == -1:
            i -= 1
            continue

        diff = ls[swap_idx][1] - ls[i][1]
        ls[swap_idx][0], ls[swap_idx][1] = ls[i][0], ls[i][1]
        ls[i][0] = -1
        if diff >= 0:
            ls.insert(swap_idx + 1, [-1, diff])

        i -= 1

    result = 0
    count = 0
    for v in ls:
        for _ in range(v[1]):
            result += count * (v[0] if v[0] != -1 else 0)
            count += 1
    return result


def main():
    print(day_9_part_1('day_9.test'))
    print(day_9_part_1('day_9.input'))
    print(day_9_part_2('day_9.test'))
    print(day_9_part_2('day_9.input'))

if __name__ == '__main__':
    main()
