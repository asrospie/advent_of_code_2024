from functools import cache


def day_11(filename, stop):
    with open(filename, 'r') as f:
        nums = [ int(c) for c in f.readline().strip().split(' ') ]

    res = 0
    for n in nums:
        res += solve(n, 0, stop)

    return res


@cache
def solve(num, acc, stop):
    if acc == stop:
        return 1
    if num == 0:
        return solve(1, acc + 1, stop)
    elif len(str(num)) % 2 == 0:
        v = str(num)
        mid = int(len(v) / 2)
        return solve(int(v[:mid]), acc + 1, stop) + solve(int(v[mid:]), acc + 1, stop)
    else:
        return solve(num * 2024, acc + 1, stop)


def main():
    print(day_11('day_11.test', 6))
    print(day_11('day_11.test', 25))
    print(day_11('day_11.input', 25))
    print(day_11('day_11.input', 75))
    

if __name__ == '__main__':
    main()
