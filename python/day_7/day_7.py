def get_nth_bit(num, n):
    mask = 1 << n
    return 1 if num & mask else 0


def parse_input(filename):
    eqs = []

    with open(filename, 'r') as f:
        for line in f.readlines():
            ans = int(line.split(':')[0])
            ops = line.split(':')[1]
            eqs.append((ans, [ int(x) for x in ops.strip().split(' ') ]))

    return eqs

def day_7_part_1(filename):
    eqs = parse_input(filename)

    result = 0
    for row in eqs:
        k, v = row
        perms = int(2 ** (len(v) - 1))
        for op in range(perms):
            solution = v[0]
            for i in range(len(v) - 1):
                if get_nth_bit(op, i) == 0:
                    solution += v[i + 1]
                else:
                    solution *= v[i + 1]
            if solution == k:
                result += k 
                break
    return result


def ternary(n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(reversed(nums))


def day_7_part_2(filename):
    eqs = parse_input(filename)
    result = 0

    for row in eqs:
        k, v = row
        perms = int(3 ** (len(v) - 1))
        for op in range(perms):
            tern = ternary(op).rjust(len(v) - 1, '0')
            solution = v[0]
            for i in range(len(v) - 1):
                if tern[i] == '0':
                    solution += v[i + 1]
                elif tern[i] == '1':
                    solution *= v[i + 1]
                elif tern[i] == '2':
                    solution = int(str(solution) + str(v[i + 1]))
            if solution == k:
                result += k 
                break


    return result


def main():
    print(day_7_part_1('day_7.test'))
    print(day_7_part_1('day_7.input'))
    print(day_7_part_2('day_7.test'))
    print(day_7_part_2('day_7.input'))

if __name__ == '__main__':
    main()
