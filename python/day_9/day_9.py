def find_last(lst):
    for i, v in enumerate(lst[::-1]):
        if v != '.':
            return len(lst) - 1 - i
    return -1


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

    print(ls)

    i = 0
    while i < len(ls):
        if ls[i][0] != -1:
            i += 1
            continue

        swap_idx = -1
        # find fitting file
        for j, v in enumerate(ls[::-1]):
            if v[0] != -1 and v[1] <= ls[i][1]:
                swap_idx = len(ls) - 1 - j
                break
        if swap_idx == -1:
            i += 1
            continue

        # swap values
        diff = ls[i][1] - ls[swap_idx][1]
        print(f'{ls[i]} :: {ls[swap_idx]}')
        ls[i] = ls[swap_idx]
        ls[swap_idx][0] = -1
        if diff != 0:
            ls.insert(i + 1, [-1, diff])
            i += 1
        i += 1

    print(ls)

    result = 0
    return result


def main():
    # print(day_9_part_1('day_9.test'))
    # print(day_9_part_1('day_9.input'))
    print(day_9_part_2('day_9.test'))
    # print(day_9_part_2('day_9.input'))

if __name__ == '__main__':
    main()
