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
    ls = parse_input(filename)

    for i, c in enumerate(ls):
        if c != '.':
            continue

        # get idxs of '.'
        idxs, cnt = [], 0
        while c[cnt + i] == '.':
            idxs.append(i + cnt)
            cnt += 1

        # find file that can fit
    result = 0
    for i, v in enumerate(ls):
        if v == '.':
            continue
        result += i * int(v)

    return result


def main():
    # print(day_9_part_1('day_9.test'))
    # print(day_9_part_1('day_9.input'))
    print(day_9_part_2('day_9.test'))
    # print(day_9_part_2('day_9.input'))

if __name__ == '__main__':
    main()
